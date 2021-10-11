import configparser as cfg
from debugger import *
from debugger import *

log('Started', 'cfg_parser.py')


def type_var(variable):
    if variable.isdigit():
        return int(variable)
    elif len(variable.split('.')) == 2:
        if variable.split('.')[0].isdigit() and variable.split('.')[0].isdigit():
            return float(variable)
    else:
        return variable


def parse(path, section='all'):
    file = cfg.ConfigParser()
    with open(path) as fp:
        file.read_file(fp)
    if section in file.sections():
        return file.items(section)
    elif section == 'all':
        returned = {}
        for section in file.sections():
            temp = {}
            for parameter in file.items(section):
                temp[parameter[0]] = type_var(parameter[1])
            returned[section] = temp
        return returned
    else:
        print(f'Секция {section} отсутствует')
        return
