# -*- coding: utf-8 -*-
"""Back-port compiler for Python 3.8 positional-only parameter syntax."""

import argparse
import contextlib
import glob
import locale
import os
import re
import shutil
import sys
import uuid

import parso
import tbtrim

__all__ = ['poseur', 'convert', 'decorator']  # pylint: disable=undefined-all-variable

# multiprocessing may not be supported
try:        # try first
    import multiprocessing
except ImportError:  # pragma: no cover
    multiprocessing = None
else:       # CPU number if multiprocessing supported
    if os.name == 'posix' and 'SC_NPROCESSORS_CONF' in os.sysconf_names:  # pragma: no cover
        CPU_CNT = os.sysconf('SC_NPROCESSORS_CONF')
    elif hasattr(os, 'sched_getaffinity'):  # pragma: no cover
        CPU_CNT = len(os.sched_getaffinity(0))  # pylint: disable=E1101
    else:  # pragma: no cover
        CPU_CNT = os.cpu_count() or 1
finally:    # alias and aftermath
    mp = multiprocessing
    del multiprocessing

# version string
__version__ = '0.4.3'

# from configparser
BOOLEAN_STATES = {'1': True, '0': False,
                  'yes': True, 'no': False,
                  'true': True, 'false': False,
                  'on': True, 'off': False}

# environs
LOCALE_ENCODING = locale.getpreferredencoding(False)

# macros
grammar_regex = re.compile(r"grammar(\d)(\d)\.txt")
POSEUR_VERSION = sorted(filter(lambda version: version >= '3.8',  # when Python starts to have positional-only arguments
                               map(lambda path: '%s.%s' % grammar_regex.match(os.path.split(path)[1]).groups(),
                                   glob.glob(os.path.join(parso.__path__[0], 'python', 'grammar??.txt')))))
del grammar_regex


class ConvertError(SyntaxError):
    """Parso syntax error."""


class EnvironError(EnvironmentError):
    """Invalid environment."""


###############################################################################
# Traceback trim (tbtrim)

# root path
ROOT = os.path.dirname(os.path.realpath(__file__))


def predicate(filename):  # pragma: no cover
    if os.path.basename(filename) == 'poseur.py':
        return True
    return ROOT in os.path.realpath(filename)


tbtrim.set_trim_rule(predicate, strict=True, target=(ConvertError, EnvironError))

###############################################################################
# UUID 4 generator wrapper


class UUID4Generator:
    """UUID 4 generator wrapper to prevent UUID collisions."""

    def __init__(self, dash=True):
        """Constructor of UUID 4 generator wrapper.
        Args:
         - `dash` -- `bool`, whether the generated UUID string has dashes or not
        """
        self.used_uuids = set()
        self.dash = dash

    def gen(self):
        """Generate a new UUID 4 string that is guaranteed not to collide with used UUIDs.
        Returns:
         - `str` -- a new UUID 4 string
        """
        while True:
            nuid = uuid.uuid4()
            nuid = str(nuid) if self.dash else nuid.hex
            if nuid not in self.used_uuids:
                break
        self.used_uuids.add(nuid)
        return nuid


# Initialise a UUID4Generator for filename UUIDs.
uuid_gen = UUID4Generator(dash=True)

###############################################################################
# Positional-only decorator

# cf. https://mail.python.org/pipermail/python-ideas/2017-February/044888.html
_decorator = '''\
def %(decorator)s(*poseur):
%(tabsize)s"""Positional-only arguments runtime checker."""
%(tabsize)simport functools
%(tabsize)sdef caller(func):
%(tabsize)s%(tabsize)s@functools.wraps(func)
%(tabsize)s%(tabsize)sdef wrapper(*args, **kwargs):
%(tabsize)s%(tabsize)s%(tabsize)sposeur_args = set(poseur).intersection(kwargs)
%(tabsize)s%(tabsize)s%(tabsize)sif poseur_args:
%(tabsize)s%(tabsize)s%(tabsize)s%(tabsize)sraise TypeError('%%s() got some positional-only arguments passed as keyword arguments: %%r' %% (func.__name__, ', '.join(poseur_args)))
%(tabsize)s%(tabsize)s%(tabsize)sreturn func(*args, **kwargs)
%(tabsize)s%(tabsize)sreturn wrapper
%(tabsize)sreturn caller
'''.splitlines()  # `str.splitlines` will remove trailing newline

exec(os.linesep.join(_decorator) % dict(decorator='decorator', tabsize='\t'.expandtabs(4)))

###############################################################################
# Main convertion implementation


def parse(string, source):
    """Parse source string.

    Args:
     - `string` -- `str`, context to be converted
     - `source` -- `str`, source of the context

    Envs:
     - `POSEUR_VERSION` -- convert against Python version (same as `--python` option in CLI)

    Returns:
     - `parso.python.tree.Module` -- parso AST

    Raises:
     - `ConvertError` -- when source code contains syntax errors

    """
    grammar = parso.load_grammar(version=os.getenv('POSEUR_VERSION', POSEUR_VERSION[-1]))
    module = grammar.parse(string, error_recovery=True)

    # suppress parso debug outputs
    # see https://github.com/davidhalter/parso/commit/ee2995c1108028cd8c6d56df3a00170c93dc9ce6
    # TODO: remove this redirect after a new version of parso is released
    with open(os.devnull, 'w') as nul_file:
        with contextlib.redirect_stdout(nul_file):
            errors = grammar.iter_errors(module)

    if errors:
        error_messages = '\n'.join('[L%dC%d] %s' % (*error.start_pos, error.message) for error in errors)
        raise ConvertError('source file %r contains following syntax errors:\n' % source + error_messages)

    return module


def decorate_lambdef(parameters, lambdef):
    """Append poseur decorator to lambda definition.

    Args:
     - `parameters` -- `List[parso.python.tree.Param]`, extracted positional-only arguments
     - `lambdef` -- `str`, converted lambda string

    Envs:
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)

    Returns:
     - `str` -- decorated lambda definition

    """
    POSEUR_DECORATOR = os.getenv('POSEUR_DECORATOR', __poseur_decorator__)

    match_prefix = re.match(r'^(?P<prefix>\s*).*?', lambdef, re.DOTALL | re.MULTILINE)
    prefix = '' if match_prefix is None else match_prefix.group('prefix')

    match_suffix = re.match(r'.*?(?P<suffix>\s*)$', lambdef, re.DOTALL | re.MULTILINE)
    suffix = '' if match_suffix is None else match_suffix.group('suffix')

    return '%s%s(%s)(%s)%s' % (prefix,
                               POSEUR_DECORATOR,
                               ', '.join(map(lambda param: repr(param.name.value), parameters)),
                               lambdef.strip(),
                               suffix)


def dismiss_lambdef(node):
    """Dismiss positional-only arguments syntax.

    Args:
     - `node` -- `parso.python.tree.Lambda`, AST of lambda parameters

    Envs:
     - `POSEUR_LINTING` -- lint converted codes (same as `--linting` option in CLI)

    Returns:
     - `str` -- converted lambda definition

    """
    params = ''
    prefix = ''
    suffix = ''

    flag_param = False
    flag_suite = False
    for child in node.children:
        # <Param: ...>
        if child.type == 'param':
            flag_param = True
            if child.default is None:
                params += child.get_code()
            else:
                params += walk(child)
        # lambda parameters
        elif flag_param:
            # <Operator: />
            if child.type == 'operator' and child.value == '/':
                params += child.get_code().replace('/', '')
            # <Operator: :>
            elif child.type == 'operator' and child.value == ':':
                flag_param = False
                flag_suite = True
                suffix += child.get_code()
            # <Operator: *> / <Operator: ,> / <Param: ...>
            else:
                params += child.get_code()
        # lambda suite
        elif flag_suite:
            suffix += walk(child)
        # lambda declration
        else:
            prefix += child.get_code()

    POSEUR_LINTING = BOOLEAN_STATES.get(os.getenv('POSEUR_LINTING', '0').casefold(), False)
    if POSEUR_LINTING:
        params = ' ' + ', '.join(filter(None, map(lambda s: s.strip(), params.split(','))))
    else:
        params = ','.join(filter(lambda s: s.strip(), params.split(',')))

    return prefix + params + suffix


def extract_lambdef(node):
    """Extract positional-only arguments from lambda definition.

    Args:
     - `node` -- `parso.python.tree.Lambda`, AST of lambda definition

    Returns:
     - `List[parso.python.tree.Param]` -- extracted positional-only arguments

    """
    pos_only = list()

    pos_temp = list()
    for child in node.children:
        if child.type == 'param':
            pos_temp.append(child)
        elif child.type == 'operator' and child.value == '/':
            pos_only.extend(pos_temp)
            break

    return pos_only


def process_lambdef(node, flag):
    """Process lambda definition.

    Args:
     - `node` -- `parso.python.tree.Lambda`, lambda AST
     - `flag` -- `bool`, dismiss runtime checks for positional-only arguments (same as `--dismiss` option in CLI)

    Envs:
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)

    Returns:
     - `str` -- processed source string

    """
    # string buffer
    string = ''

    parameters = extract_lambdef(node)
    if parameters:
        lambdef = dismiss_lambdef(node)
        if not flag:
            lambdef = decorate_lambdef(parameters, lambdef)
        string += lambdef
    else:
        string += dismiss_lambdef(node)
    return string


def decorate_funcdef(parameters, column, funcdef):
    """Append poseur decorator to function definition.

    Args:
     - `parameters` -- `List[parso.python.tree.Param]`, extracted positional-only arguments
     - `column` -- `int`, indentation of function definition
     - `funcdef` -- `str`, converted function string

    Envs:
     - `POSEUR_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)

    Returns:
     - `str` -- decorated function definition

    """
    POSEUR_LINESEP = guess_linesep(parameters[0])
    POSEUR_DECORATOR = os.getenv('POSEUR_DECORATOR', __poseur_decorator__)

    prefix = ''
    suffix = ''
    deflag = False

    for line in funcdef.splitlines(True):
        if re.match(r'^\s*(async\s+)?def\s', line) is not None:
            deflag = True
        if deflag:
            suffix += line
        else:
            prefix += line

    return '%s%s@%s(%s)%s%s' % (prefix,
                                '\t'.expandtabs(column),
                                POSEUR_DECORATOR,
                                ', '.join(map(lambda param: repr(param.name.value), parameters)),
                                POSEUR_LINESEP,
                                suffix)


def dismiss_funcdef(node):
    """Dismiss positional-only arguments syntax.

    Args:
     - `node` -- `parso.python.tree.PythonNode`, AST of function parameters

    Envs:
     - `POSEUR_LINTING` -- lint converted codes (same as `--linting` option in CLI)

    Returns:
     - `str` -- converted parameters string

    """
    # <Operator: (>
    string = node.children[0].get_code()

    params = ''
    for child in node.children[1:-1]:
        # <Operator: />
        if child.type == 'operator' and child.value == '/':
            params += child.get_code().replace('/', '')
        elif child.type == 'param':
            if child.default is None:
                params += child.get_code()
            else:
                params += walk(child)
        # <Operator: *> / <Operator: ,>
        else:
            params += child.get_code()

    POSEUR_LINTING = BOOLEAN_STATES.get(os.getenv('POSEUR_LINTING', '0').casefold(), False)
    if POSEUR_LINTING:
        string += ', '.join(filter(None, map(lambda s: s.strip(), params.split(','))))
    else:
        string += ','.join(filter(lambda s: s.strip(), params.split(',')))

    # <Operator: )>
    string += node.children[-1].get_code()

    return string


def extract_funcdef(node):
    """Extract positional-only arguments from function parameters.

    Args:
     - `node` -- `parso.python.tree.PythonNode`, AST of function parameters

    Returns:
     - `List[parso.python.tree.Param]` -- extracted positional-only arguments

    """
    pos_only = list()

    pos_temp = list()
    for child in node.children[1:-1]:
        if child.type == 'param':
            pos_temp.append(child)
        elif child.type == 'operator' and child.value == '/':
            pos_only.extend(pos_temp)
            break

    return pos_only


def process_funcdef(node, flag, *, async_ctx=None):
    """Process function definition.

    Args:
     - `node` -- `parso.python.tree.Function`, function AST
     - `flag` -- `bool`, dismiss runtime checks for positional-only arguments

    Kwds:
     - `async_ctx` -- `parso.python.tree.Keyword`, `async` keyword AST node

    Envs:
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)

    Returns:
     - `str` -- processed source string

    """
    # string buffer
    string = ''

    if async_ctx is None:
        funcdef = ''
    else:
        funcdef = async_ctx.get_code()

    for child in node.children:
        if child.type == 'parameters':
            parameters = extract_funcdef(child)
            funcdef += dismiss_funcdef(child)
        else:  # suite / ...
            funcdef += walk(child)
    if parameters and (not flag):
        if async_ctx is None:
            column = node.get_first_leaf().column
        else:
            column = async_ctx.column
        string += decorate_funcdef(parameters, column, funcdef)
    else:
        string += funcdef
    return string


def check_lambdef(node):
    """Check if lambda definition contains positional-only arguments.

    Args:
     - `node` -- `parso.python.tree.Lambda`, lambda definition

    Returns:
     - `bool` -- if lambda definition contains positional-only arguments

    """
    param = False
    suite = False
    for child in node.children:
        if child.type == 'param':
            if child.default is not None:
                if has_poseur(child.default):
                    return True
            param = True
        elif child.type == 'operator' and child.value == ':':
            param = False
            suite = True
        elif param and child.type == 'operator' and child.value == '/':
            return True
        elif suite and has_poseur(child):
            return True
    return False


def check_funcdef(node):
    """Check if function definition contains positional-only arguments.

    Args:
     - `node` -- `parso.python.tree.Function`, function definition

    Returns:
     - `bool` -- if function definition contains positional-only arguments

    """
    for child in node.children:
        if child.type == 'parameters':
            for param in child.children[1:-1]:
                if param.type == 'operator':
                    if param.value == '/':
                        return True
                    continue
                if param.default is not None and has_poseur(param.default):
                    return True
        elif has_poseur(child):  # suite / ...
            return True
    return False


def has_poseur(node):
    """Check if node has function/lambda definitions.

    Args:
     - `node` -- `Union[parso.python.tree.PythonNode, parso.python.tree.PythonLeaf]`, node to search

    Return:
     - `bool` -- if node has function/lambda definitions

    """
    if node.type == 'funcdef':
        return check_funcdef(node)
    if node.type == 'lambdef':
        return check_lambdef(node)
    if not hasattr(node, 'children'):
        return False
    return any(map(has_poseur, node.children))


def find_poseur(node, root=0):
    """Find node to insert poseur decorator.

    Args:
     - `node` -- `parso.python.tree.Module`, parso AST
     - `root` -- `int`, index for insertion (based on `node`)

    Returns:
     - `int` -- index for insertion (based on `node`)

    """
    for index, child in enumerate(node.children, start=1):
        if has_poseur(child):
            return root
        if child.get_first_leaf().column == 0:
            root = index
    return -1


def check_suffix(string):
    """Strip comments from string.

    Args:
     - `string` -- `str`, buffer string

    Returns:
     - `str` -- prefix comments
     - `str` -- suffix strings

    """
    prefix = ''
    suffix = ''

    lines = iter(string.splitlines(True))
    for line in lines:
        if line.strip().startswith('#'):
            prefix += line
            continue
        suffix += line
        break

    for line in lines:
        suffix += line
    return prefix, suffix


def guess_tabsize(node):
    """Check indentation tab size.

    Args:
        - `node` -- `Union[parso.python.tree.PythonNode, parso.python.tree.PythonLeaf]`, parso AST

    Env:
        - `POSEUR_TABSIZE` -- indentation tab size (same as `--tabsize` option in CLI)

    Returns:
        - `int` -- indentation tab size

    """
    for child in node.children:
        if child.type != 'suite':
            if hasattr(child, 'children'):
                return guess_tabsize(child)
            continue
        return child.children[1].get_first_leaf().column
    return int(os.getenv('POSEUR_TABSIZE', __poseur_tabsize__))


def guess_linesep(node):
    """Guess line separator based on source code.

    Args:
        - `node` -- `Union[parso.python.tree.PythonNode, parso.python.tree.PythonLeaf]`, parso AST

    Envs:
        - `POSEUR_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)

    Returns:
        - `str` -- line separator

    """
    root = node.get_root_node()
    code = root.get_code()

    pool = {
        '\r': 0,
        '\r\n': 0,
        '\n': 0,
    }
    for line in code.splitlines(True):
        if line.endswith('\r'):
            pool['\r'] += 1
        elif line.endswith('\r\n'):
            pool['\r\n'] += 1
        else:
            pool['\n'] += 1

    sort = sorted(pool, key=lambda k: pool[k])
    if pool[sort[0]] > pool[sort[1]]:
        return sort[0]

    env = os.getenv('POSEUR_LINESEP', os.linesep)
    env_name = env.upper()
    if env_name == 'CR':
        return '\r'
    if env_name == 'CRLF':
        return '\r\n'
    if env_name == 'LF':
        return '\n'
    if env in ['\r', '\r\n', '\n']:
        return env
    raise EnvironError('invlid line separator %r' % env)


def process_module(node):
    """Walk top nodes of the AST module.

    Args:
     - `node` -- `parso.python.tree.Module`, parso AST

    Envs:
     - `POSEUR_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
     - `POSEUR_LINTING` -- lint converted codes (same as `--linting` option in CLI)
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)
     - `POSEUR_TABSIZE` -- indentation tab size (same as `--tabsize` option in CLI)

    Returns:
     - `str` -- processed source string

    """
    prefix = ''
    suffix = ''

    postmt = find_poseur(node)
    for index, child in enumerate(node.children):
        if index < postmt:
            prefix += walk(child)
        else:
            bufpre, bufsuf = check_suffix(walk(child))
            prefix += bufpre
            suffix += bufsuf

    if postmt >= 0:
        POSEUR_TABSIZE = guess_tabsize(node)
        POSEUR_LINESEP = guess_linesep(node)
        POSEUR_DECORATOR = os.getenv('POSEUR_DECORATOR', __poseur_decorator__)

        middle = POSEUR_LINESEP.join(_decorator) % dict(
            decorator=POSEUR_DECORATOR,
            tabsize='\t'.expandtabs(POSEUR_TABSIZE),
        )
        if not prefix:
            middle = middle.lstrip()
        if not suffix:
            middle = middle.rstrip()

        POSEUR_LINTING = BOOLEAN_STATES.get(os.getenv('POSEUR_LINTING', '0').casefold(), False)
        if POSEUR_LINTING:
            if prefix:
                if prefix.endswith(POSEUR_LINESEP * 2):
                    pass
                elif prefix.endswith(POSEUR_LINESEP):
                    middle = POSEUR_LINESEP + middle
                else:
                    middle = POSEUR_LINESEP * 2 + middle

            if suffix:
                if suffix.startswith(POSEUR_LINESEP * 2):
                    pass
                elif suffix.startswith(POSEUR_LINESEP):
                    middle += POSEUR_LINESEP
                else:
                    middle += POSEUR_LINESEP * 2

        poflag = False
        string = prefix
        for line in suffix.splitlines(True):
            stripped = line.strip()
            if poflag:
                string += line
            elif (not stripped) or stripped.startswith('#'):
                string += line
            else:
                poflag = True
                string += middle + line
        return string
    return prefix + suffix


def walk(node):
    """Walk parso AST.

    Args:
     - `node` -- `Union[parso.python.tree.Module, parso.python.tree.PythonNode, parso.python.tree.PythonLeaf]`,
                 parso AST

    Envs:
     - `POSEUR_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
     - `POSEUR_DISMISS` -- dismiss runtime checks for positional-only arguments (same as `--dismiss` option in CLI)
     - `POSEUR_LINTING` -- lint converted codes (same as `--linting` option in CLI)
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)

    Returns:
     - `str` -- converted string

    """
    POSEUR_DISMISS = BOOLEAN_STATES.get(os.getenv('POSEUR_DISMISS', '0').casefold(), False)
    if isinstance(node, parso.python.tree.Module) and (not POSEUR_DISMISS):
        return process_module(node)

    # string buffer
    string = ''

    if node.type == 'funcdef':
        return process_funcdef(node, flag=POSEUR_DISMISS)

    if node.type == 'async_stmt':
        child_1st = node.children[0]
        child_2nd = node.children[1]

        flag_1st = child_1st.type == 'keyword' and child_1st.value == 'async'
        flag_2nd = child_2nd.type == 'funcdef'

        if flag_1st and flag_2nd:  # pragma: no cover
            return process_funcdef(child_2nd, flag=POSEUR_DISMISS, async_ctx=child_1st)

    if node.type == 'lambdef':
        return process_lambdef(node, flag=POSEUR_DISMISS)

    if isinstance(node, parso.python.tree.PythonLeaf):
        string += node.get_code()

    if hasattr(node, 'children'):
        for child in node.children:
            string += walk(child)

    return string


def convert(string, source='<unknown>'):
    """The main conversion process.

    Args:
     - `string` -- `str`, context to be converted
     - `source` -- `str`, source of the context

    Envs:
     - `POSEUR_VERSION` -- convert against Python version (same as `--python` option in CLI)
     - `POSEUR_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
     - `POSEUR_DISMISS` -- dismiss runtime checks for positional-only arguments (same as `--dismiss` option in CLI)
     - `POSEUR_LINTING` -- lint converted codes (same as `--linting` option in CLI)
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)

    Returns:
     - `str` -- converted string

    """
    # parse source string
    module = parse(string, source)

    # convert source string
    string = walk(module)

    # return converted string
    return string


def poseur(filename):
    """Wrapper works for conversion.

    Args:
     - `filename` -- `str`, file to be converted

    Envs:
     - `POSEUR_QUIET` -- run in quiet mode (same as `--quiet` option in CLI)
     - `POSEUR_ENCODING` -- encoding to open source files (same as `--encoding` option in CLI)
     - `POSEUR_VERSION` -- convert against Python version (same as `--python` option in CLI)
     - `POSEUR_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
     - `POSEUR_DISMISS` -- dismiss runtime checks for positional-only arguments (same as `--dismiss` option in CLI)
     - `POSEUR_LINTING` -- lint converted codes (same as `--linting` option in CLI)
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)

    """
    POSEUR_QUIET = BOOLEAN_STATES.get(os.getenv('POSEUR_QUIET', '0').casefold(), False)
    if not POSEUR_QUIET:  # pragma: no cover
        print('Now converting %r...' % filename)

    # fetch encoding
    encoding = os.getenv('POSEUR_ENCODING', LOCALE_ENCODING)

    # file content
    with open(filename, 'r', encoding=encoding, newline='') as file:
        text = file.read()

    # do the dirty things
    text = convert(text, filename)

    # dump back to the file
    with open(filename, 'w', encoding=encoding, newline='') as file:
        file.write(text)


###############################################################################
# CLI & entry point

# default values
__cwd__ = os.getcwd()
__archive__ = os.path.join(__cwd__, 'archive')
__poseur_version__ = os.getenv('POSEUR_VERSION', POSEUR_VERSION[-1])
__poseur_encoding__ = os.getenv('POSEUR_ENCODING', LOCALE_ENCODING)
__poseur_linesep__ = os.getenv('POSEUR_LINESEP', os.linesep)
__poseur_decorator__ = os.getenv('POSEUR_DECORATOR', '__poseur_decorator')
__poseur_tabsize__ = os.getenv('POSEUR_TABSIZE', '4')


def get_parser():
    """Generate CLI parser.

    Returns:
     - `argparse.ArgumentParser` -- CLI parser for poseur

    """
    parser = argparse.ArgumentParser(prog='poseur',
                                     usage='poseur [options] <python source files and folders...>',
                                     description='Back-port compiler for Python 3.8 positional-only parameters.')
    parser.add_argument('-V', '--version', action='version', version=__version__)
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='run in quiet mode')

    archive_group = parser.add_argument_group(title='archive options',
                                              description="duplicate original files in case there's any issue")
    archive_group.add_argument('-na', '--no-archive', action='store_false', dest='archive',
                               help='do not archive original files')
    archive_group.add_argument('-p', '--archive-path', action='store', default=__archive__, metavar='PATH',
                               help='path to archive original files (%(default)s)')

    convert_group = parser.add_argument_group(title='convert options',
                                              description='compatibility configuration for non-unicode files')
    convert_group.add_argument('-c', '--encoding', action='store', default=__poseur_encoding__, metavar='CODING',
                               help='encoding to open source files (%(default)s)')
    convert_group.add_argument('-v', '--python', action='store', metavar='VERSION',
                               default=__poseur_version__, choices=POSEUR_VERSION,
                               help='convert against Python version (%(default)s)')
    convert_group.add_argument('-s', '--linesep', action='store', default=__poseur_linesep__, metavar='SEP',
                               help='line separator to process source files (%(default)r)')
    convert_group.add_argument('-d', '--dismiss', action='store_true',
                               help='dismiss runtime checks for positional-only parameters')
    convert_group.add_argument('-nl', '--no-linting', action='store_false', dest='linting',
                               help='do not lint converted codes')
    convert_group.add_argument('-r', '--decorator', action='store', default=__poseur_decorator__, metavar='VAR',
                               help='name of decorator for runtime checks (`%(default)s`)')
    convert_group.add_argument('-t', '--tabsize', action='store', default=__poseur_tabsize__, metavar='INDENT',
                               help='indentation tab size (%(default)s)', type=int)

    parser.add_argument('file', nargs='+', metavar='SOURCE', default=__cwd__,
                        help='python source files and folders to be converted (%(default)s)')

    return parser


def find(root):  # pragma: no cover
    """Recursively find all files under root.

    Args:
     - `root` -- `os.PathLike`, root path to search

    Returns:
     - `Generator[str, None, None]` -- yield all files under the root path

    """
    file_list = list()
    for entry in os.scandir(root):
        if entry.is_dir():
            file_list.extend(find(entry.path))
        elif entry.is_file():
            file_list.append(entry.path)
        elif entry.is_symlink():  # exclude symbolic links
            continue
    yield from file_list


def rename(path, root):
    """Rename file for archiving.

    Args:
     - `path` -- `os.PathLike`, file to rename
     - `root` -- `os.PathLike`, archive path

    Returns:
     - `str` -- the archiving path

    """
    stem, ext = os.path.splitext(path)
    name = '%s-%s%s' % (stem, uuid_gen.gen(), ext)
    return os.path.join(root, name)


def main(argv=None):
    """Entry point for poseur.

    Args:
     - `argv` -- `List[str]`, CLI arguments (default: None)

    Envs:
     - `POSEUR_QUIET` -- run in quiet mode (same as `--quiet` option in CLI)
     - `POSEUR_ENCODING` -- encoding to open source files (same as `--encoding` option in CLI)
     - `POSEUR_VERSION` -- convert against Python version (same as `--python` option in CLI)
     - `POSEUR_LINESEP` -- line separator to process source files (same as `--linesep` option in CLI)
     - `POSEUR_DISMISS` -- dismiss runtime checks for positional-only arguments (same as `--dismiss` option in CLI)
     - `POSEUR_LINTING` -- lint converted codes (same as `--linting` option in CLI)
     - `POSEUR_DECORATOR` -- name of decorator for runtime checks (same as `--decorator` option in CLI)
     - `POSEUR_TABSIZE` -- indentation tab size (same as `--tabsize` option in CLI)

    """
    parser = get_parser()
    args = parser.parse_args(argv)

    # set up variables
    ARCHIVE = args.archive_path
    os.environ['POSEUR_VERSION'] = args.python
    os.environ['POSEUR_ENCODING'] = args.encoding
    os.environ['POSEUR_DECORATOR'] = args.decorator
    os.environ['POSEUR_TABSIZE'] = str(args.tabsize)
    POSEUR_QUIET = os.getenv('POSEUR_QUIET')
    os.environ['POSEUR_QUIET'] = '1' if args.quiet else ('0' if POSEUR_QUIET is None else POSEUR_QUIET)
    POSEUR_DISMISS = os.getenv('POSEUR_DISMISS')
    os.environ['POSEUR_DISMISS'] = '1' if args.dismiss else ('0' if POSEUR_DISMISS is None else POSEUR_DISMISS)
    POSEUR_LINTING = os.getenv('POSEUR_LINTING')
    os.environ['POSEUR_LINTING'] = '1' if args.linting else ('0' if POSEUR_LINTING is None else POSEUR_LINTING)

    linesep = args.linesep.upper()
    if linesep == 'CR':
        os.environ['POSEUR_LINESEP'] = '\r'
    elif linesep == 'CRLF':
        os.environ['POSEUR_LINESEP'] = '\r\n'
    elif linesep == 'LF':
        os.environ['POSEUR_LINESEP'] = '\n'
    elif args.linesep in ['\r', '\r\n', '\n']:
        os.environ['POSEUR_LINESEP'] = args.linesep
    else:
        raise EnvironError('invalid line separator %r' % args.linesep)

    # make archive directory
    if args.archive:  # pragma: no cover
        os.makedirs(ARCHIVE, exist_ok=True)

    # fetch file list
    filelist = list()
    for path in args.file:
        if os.path.isfile(path):
            if args.archive:  # pragma: no cover
                dest = rename(path, root=ARCHIVE)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy(path, dest)
            filelist.append(path)
        if os.path.isdir(path):  # pragma: no cover
            if args.archive:
                shutil.copytree(path, rename(path, root=ARCHIVE))
            filelist.extend(find(path))

    # check if file is Python source code
    ispy = lambda file: (os.path.isfile(file) and (os.path.splitext(file)[1] in ('.py', '.pyw')))
    filelist = sorted(filter(ispy, filelist))

    # if no file supplied
    if not filelist:  # pragma: no cover
        parser.error('argument PATH: no valid source file found')

    # process files
    if mp is None or CPU_CNT <= 1:
        [poseur(filename) for filename in filelist]  # pylint: disable=expression-not-assigned # pragma: no cover
    else:
        with mp.Pool(processes=CPU_CNT) as pool:
            pool.map(poseur, filelist)


if __name__ == '__main__':
    sys.exit(main())
