'''
Configuration content and parsing functions.
'''

import os

import toml

from luculia import tools

ENVIRON = 'LUCULIA'
DEFAULT = '~/.luculia'

CONFIGURATION = '''
# # # # # # # # # # # # # # # #
# Luculia Configuration File. #
# # # # # # # # # # # # # # # #

# The path to your notes directory.
directory = "~/notes"

# The extension your note files use.
extension = "txt"
'''

def parse():
    '''
    Return a dict of parsed configuration data.
    '''

    orig = os.environ.get(ENVIRON, DEFAULT)
    path = tools.path.expand(orig)
    data = toml.loads(tools.file.read(path))

    return {**data,
        'directory': tools.path.expand(data['directory']),
        'extension': data['extension'].lstrip('.'),
    }
