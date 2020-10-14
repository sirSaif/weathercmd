import os
import re
import inspect



def _get_parser_list(dir_name):
    # list of all valid parser files from parsers dir.
    files = [f.replace('.py', '') for f in os.listdir(dir_name)
             if not f.startswith('__')
             and not os.path.isdir(os.path.join(dir_name, f))]
    return files


def _import_parsers(parser_files):
    m = re.compile('.+parser$', re.I)

    _modules = __import__('src.parsers', globals(), locals(), parser_files, 0)

    _parsers = [(k, v) for k, v in inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]

    _classes = dict()
    for key, value in _parsers:
        _classes.update({k: v for k, v in inspect.getmembers(value)
                         if inspect.isclass(v) and m.match(k)})
    return _classes


def load(dir_name):
    # load all parser classes in parsers directory
    parser_files = _get_parser_list(dir_name)
    return _import_parsers(parser_files)

print(load("../parsers"))
