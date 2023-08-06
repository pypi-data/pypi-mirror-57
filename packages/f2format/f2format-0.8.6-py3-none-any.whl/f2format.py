# -*- coding: utf-8 -*-
"""Back-port compiler for Python 3.6 f-string literals."""

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

__all__ = ['f2format', 'convert', 'ConvertError']

# multiprocessing may not be supported
try:        # try first
    import multiprocessing
except ImportError:  # pragma: no cover
    multiprocessing = None
else:       # CPU number if multiprocessing supported
    if os.name == 'posix' and 'SC_NPROCESSORS_CONF' in os.sysconf_names:  # pragma: no cover
        CPU_CNT = os.sysconf('SC_NPROCESSORS_CONF')
    elif 'sched_getaffinity' in os.__all__:  # pragma: no cover
        CPU_CNT = len(os.sched_getaffinity(0))  # pylint: disable=E1101
    else:  # pragma: no cover
        CPU_CNT = os.cpu_count() or 1
finally:    # alias and aftermath
    mp = multiprocessing
    del multiprocessing

# version string
__version__ = '0.8.6'

# from configparser
BOOLEAN_STATES = {'1': True, '0': False,
                  'yes': True, 'no': False,
                  'true': True, 'false': False,
                  'on': True, 'off': False}

# environs
LOCALE_ENCODING = locale.getpreferredencoding(False)

# macros
grammar_regex = re.compile(r"grammar(\d)(\d)\.txt")
F2FORMAT_VERSION = sorted(filter(lambda version: version >= '3.6',  # when Python starts to have f-string
                                 map(lambda path: '%s.%s' % grammar_regex.match(os.path.split(path)[1]).groups(),
                                     glob.glob(os.path.join(parso.__path__[0], 'python', 'grammar??.txt')))))
del grammar_regex


class ConvertError(SyntaxError):
    """Parso syntax error."""


###############################################################################
# Traceback trim (tbtrim)

# root path
ROOT = os.path.dirname(os.path.realpath(__file__))


def predicate(filename):  # pragma: no cover
    if os.path.basename(filename) == 'f2format':
        return True
    return ROOT in os.path.realpath(filename)


tbtrim.set_trim_rule(predicate, strict=True, target=ConvertError)

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
# Main convertion implementation


def parse(string, source):
    """Parse source string.

    Args:
     - `string` -- `str`, context to be converted
     - `source` -- `str`, source of the context

    Envs:
     - `F2FORMAT_VERSION` -- convert against Python version (same as `--python` option in CLI)

    Returns:
     - `parso.python.tree.Module` -- parso AST

    Raises:
     - `ConvertError` -- when source code contains syntax errors

    """
    grammar = parso.load_grammar(version=os.getenv('F2FORMAT_VERSION', F2FORMAT_VERSION[-1]))
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


def extract(node):
    """Extract f-string components.

    Args:
     - `node` -- `parso.python.tree.PythonNode`, parso AST for f-string

    Returns:
     - `str` -- extracted f-string string components
     - `List[str]` -- extracted f-string expressions

    """
    # FStringStart
    string = re.sub(r'[fF]', '', node.children[0].get_code())

    expr_list = list()
    for child in node.children[1:-1]:
        if child.type != 'fstring_expr':
            string += child.get_code()
            continue

        # <Operator: {>
        string += '{'

        expr_str = ''
        spec_str = ''
        for expr in child.children[1:-1]:
            # conversion
            if expr.type == 'fstring_conversion':
                string += expr.get_code().strip()
            # format specification
            elif expr.type == 'fstring_format_spec':
                for spec in expr.children:
                    if spec.type != 'fstring_expr':
                        string += spec.get_code().strip()
                        continue

                    # <Operator: {>
                    string += '{'

                    for spec_expr in spec.children[1:-1]:
                        if spec_expr.type == 'fstring_conversion':  # pragma: no cover
                            string += spec_expr.get_code().strip()
                        elif spec_expr.type == 'fstring_format_spec':  # pragma: no cover
                            string += spec_expr.get_code().strip()
                        elif spec_expr.type == 'testlist':  # pragma: no cover
                            spec_str += '(%s)' % spec_expr.get_code()
                        else:
                            spec_str += spec_expr.get_code()

                    # <Operator: }>
                    string += '}'
            # implicit tuple
            elif expr.type == 'testlist':
                expr_str += '(%s)' % expr.get_code()
            # embedded f-string
            elif expr.type == 'fstring':
                text, expr = extract(expr)
                expr_str += text
                if expr:
                    expr_str += '.format(%s)' % ', '.join(expr)
            # concatenable strings
            elif expr.type == 'strings':
                text_temp_list = list()
                expr_temp_list = list()
                for expr_child in expr.children:
                    if expr_child.type == 'fstring':
                        text_temp, expr_temp = extract(expr_child)
                        text_temp_list.append((True, text_temp))
                        expr_temp_list.extend(expr_temp)
                    else:
                        text_temp_list.append((False, expr_child.get_code()))
                if expr_temp_list:
                    expr_str += ''.join(map(lambda text: text[1] if text[0]
                                            else re.sub(r'([{}])', r'\1\1', text[1]), text_temp_list))
                    expr_str += '.format(%s)' % ', '.join(expr_temp_list)
                else:
                    expr_str += ''.join(map(lambda text: text[1], text_temp_list))
            # regular expression / debug f-string
            elif expr.type == 'operator' and expr.value == '=':
                next_sibling = expr.get_next_sibling()
                if (next_sibling.type == 'operator' and next_sibling.value == '}') \
                    or next_sibling.type in ['fstring_conversion', 'fstring_format_spec']:
                    expr_tmp = expr_str + expr.get_code() + re.sub(r'\S+.*$', r'', next_sibling.get_code()) + '{}'
                    expr_str = '%r.format(%s)' % (expr_tmp, expr_str)
                else:  # pragma: no cover
                    expr_str += expr.get_code()
            # regular expression
            else:
                expr_str += expr.get_code()

        if expr_str:  # pragma: no cover
            expr_list.append(expr_str)
        if spec_str:
            expr_list.append(spec_str)

        # <Operator: }>
        string += '}'

    # FStringEnd
    string += node.children[-1].get_code()

    return string, expr_list


def walk(node):
    """Walk parso AST.

    Args:
     - `node` -- `parso.python.tree.Module`, parso AST

    Returns:
     - `str` -- converted string

    """
    string = ''

    if node.type == 'strings':
        text_list = list()
        expr_list = list()
        for child in node.children:
            if child.type == 'fstring':
                text, expr = extract(child)
                text_list.append((True, text))
                expr_list.extend(expr)
            else:
                text_list.append((False, child.get_code()))
        if expr_list:
            string += ''.join(map(lambda text: text[1] if text[0] else re.sub(r'([{}])', r'\1\1', text[1]), text_list))
            string += '.format(%s)' % ', '.join(expr_list)
        else:
            string += ''.join(map(lambda text: text[1], text_list))
        return string

    if node.type == 'fstring':
        text, expr = extract(node)
        string += text
        if expr:
            string += '.format(%s)' % ', '.join(expr)
        return string

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
     - `F2FORMAT_VERSION` -- convert against Python version (same as `--python` option in CLI)

    Returns:
     - `str` -- converted string

    Raises:
     - `ConvertError` -- when `parso.ParserSyntaxError` raised

    """
    # parse source string
    module = parse(string, source)

    # convert source string
    string = walk(module)

    # return converted string
    return string


def f2format(filename):
    """Wrapper works for conversion.

    Args:
     - `filename` -- `str`, file to be converted

    Envs:
     - `F2FORMAT_QUIET` -- run in quiet mode (same as `--quiet` option in CLI)
     - `F2FORMAT_ENCODING` -- encoding to open source files (same as `--encoding` option in CLI)
     - `F2FORMAT_VERSION` -- convert against Python version (same as `--python` option in CLI)

    Raises:
     - `ConvertError` -- when `parso.ParserSyntaxError` raised

    """
    F2FORMAT_QUIET = BOOLEAN_STATES.get(os.getenv('F2FORMAT_QUIET', '0').casefold(), False)
    if not F2FORMAT_QUIET:
        print('Now converting %r...' % filename)

    # fetch encoding
    encoding = os.getenv('F2FORMAT_ENCODING')

    # file content
    with open(filename, 'r', encoding=encoding) as file:
        text = file.read()

    # do the dirty things
    text = convert(text, filename)

    # dump back to the file
    with open(filename, 'w', encoding=encoding) as file:
        file.write(text)


###############################################################################
# CLI & entry point

# default values
__cwd__ = os.getcwd()
__archive__ = os.path.join(__cwd__, 'archive')
__f2format_version__ = os.getenv('F2FORMAT_VERSION', F2FORMAT_VERSION[-1])
__f2format_encoding__ = os.getenv('F2FORMAT_ENCODING', LOCALE_ENCODING)


def get_parser():
    """Generate CLI parser.

    Returns:
     - `argparse.ArgumentParser` -- CLI parser for f2format

    """
    parser = argparse.ArgumentParser(prog='f2format',
                                     usage='f2format [options] <python source files and folders...>',
                                     description='Convert f-string to str.format for Python 3 compatibility.')
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
    convert_group.add_argument('-c', '--encoding', action='store', default=__f2format_encoding__, metavar='CODING',
                               help='encoding to open source files (%(default)s)')
    convert_group.add_argument('-v', '--python', action='store', metavar='VERSION',
                               default=__f2format_version__, choices=F2FORMAT_VERSION,
                               help='convert against Python version (%(default)s)')

    parser.add_argument('file', nargs='+', metavar='SOURCE', default=__cwd__,
                        help='python source files and folders to be converted (%(default)s)')

    return parser


def find(root):  # pragma: no cover
    """Recursively find all files under root.

    Args:
     - `root` -- os.PathLike, root path to search

    Returns:
     - `Generator[str, None, None]` -- yield all files under the root path

    """
    flst = list()
    temp = os.listdir(root)
    for file in temp:
        path = os.path.join(root, file)
        if os.path.isdir(path):
            flst.extend(find(path))
        elif os.path.isfile(path):
            flst.append(path)
        elif os.path.islink(path):  # exclude symbolic links
            continue
    yield from flst


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
    """Entry point for f2format.

    Args:
     - `argv` -- `List[str]`, CLI arguments (default: None)

    Envs:
     - `F2FORMAT_QUIET` -- run in quiet mode (same as `--quiet` option in CLI)
     - `F2FORMAT_ENCODING` -- encoding to open source files (same as `--encoding` option in CLI)
     - `F2FORMAT_VERSION` -- convert against Python version (same as `--python` option in CLI)

    Raises:
     - `ConvertError` -- when `parso.ParserSyntaxError` raised

    """
    parser = get_parser()
    args = parser.parse_args(argv)

    # set up variables
    ARCHIVE = args.archive_path
    os.environ['F2FORMAT_VERSION'] = args.python
    os.environ['F2FORMAT_ENCODING'] = args.encoding

    F2FORMAT_QUIET = os.getenv('F2FORMAT_QUIET')
    os.environ['F2FORMAT_QUIET'] = '1' if args.quiet else ('0' if F2FORMAT_QUIET is None else F2FORMAT_QUIET)

    # make archive directory
    if args.archive:
        os.makedirs(ARCHIVE, exist_ok=True)

    # fetch file list
    filelist = list()
    for path in args.file:
        if os.path.isfile(path):
            if args.archive:
                dest = rename(path, root=ARCHIVE)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy(path, dest)
            filelist.append(path)
        if os.path.isdir(path):
            if args.archive:
                shutil.copytree(path, rename(path, root=ARCHIVE))
            filelist.extend(find(path))

    # check if file is Python source code
    ispy = lambda file: (os.path.isfile(file) and (os.path.splitext(file)[1] in ('.py', '.pyw')))
    filelist = sorted(filter(ispy, filelist))

    # if no file supplied
    if not filelist:
        parser.error('argument PATH: no valid source file found')

    # process files
    if mp is None or CPU_CNT <= 1:
        [f2format(filename) for filename in filelist]  # pylint: disable=expression-not-assigned # pragma: no cover
    else:
        with mp.Pool(processes=CPU_CNT) as pool:
            pool.map(f2format, filelist)


if __name__ == '__main__':
    sys.exit(main())
