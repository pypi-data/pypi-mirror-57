'''
File system manipulation functions.
'''

import glob as glob_
import os
import shutil

from luculia import tools

OPTIONS = {'encoding': 'utf-8'}

def copy(path, name):
    '''
    Copy an existing file to a new name in the same directory, and
    return the destination path.
    '''

    dire = tools.path.dire(path)
    ext  = tools.path.ext(path)
    dest = tools.path.join(dire, f'{name}.{ext}')
    shutil.copyfile(path, dest)
    return dest

def create(path, body):
    '''
    Create a new file containing a body.
    '''

    if exists(path):
        raise tools.errs.FileExists(path)

    with open(path, 'w', **OPTIONS) as fp:
        fp.write(body)

def exists(path):
    '''
    Return True if a file exists.
    '''

    return os.path.isfile(path)

def glob(dire, pattern):
    '''
    Yield all paths in a directory matching a glob pattern.
    '''

    yield from glob_.iglob(tools.path.join(dire, pattern))

def read(path):
    '''
    Return the body of an existing file.
    '''

    with open(path, 'r', **OPTIONS) as fp:
        return fp.read()

def reext(path, ext):
    '''
    Move the file to a different extension in the same directory, and
    return the destination path.
    '''

    dire = tools.path.dire(path)
    name = tools.path.name(path)
    dest = tools.path.join(dire, f'{name}.{ext}')
    shutil.move(path, dest)
    return dest

def rename(path, name):
    '''
    Move the file to a different name in the same directory, and return
    the destination path.
    '''

    dire = tools.path.dire(path)
    ext  = tools.path.ext(path)
    dest = tools.path.join(dire, f'{name}.{ext}')
    shutil.move(path, dest)
    return dest

def update(path, body):
    '''
    Overwrite an existing file with a new body.
    '''

    if not exists(path):
        raise tools.errs.FileNotExists(path)

    with open(path, 'w', **OPTIONS) as fp:
        fp.write(body)
