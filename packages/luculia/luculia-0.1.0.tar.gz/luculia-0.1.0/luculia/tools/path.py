'''
Filepath manipulation functions.
'''

import os.path

EXPANSIONS = {
    '~': os.path.expanduser,
    '$': os.path.expandvars,
    '%': os.path.expandvars,
}

def base(path):
    '''
    Return a path's base name, with the extension.
    '''

    return os.path.basename(path)

def clean(path):
    '''
    Return a cleaned path with correct separators.
    '''

    return os.path.normpath(path)

def dire(path):
    '''
    Return a path's parent directory.
    '''

    return os.path.dirname(path)

def expand(path):
    '''
    Return a path with tildes and variables expanded.
    '''

    for char, func in EXPANSIONS.items():
        if char in path:
            path = func(path)
    return os.path.normpath(path)

def ext(path):
    '''
    Return a path's extension, without the dot.
    '''

    return os.path.splitext(path)[1].lstrip('.')

def join(*elems):
    '''
    Return a clean path joined from elements.
    '''

    return os.path.normpath(os.path.join(*elems))

def name(path):
    '''
    Return a path's base name, without the extension.
    '''

    base = os.path.basename(path)
    return os.path.splitext(base)[0]
