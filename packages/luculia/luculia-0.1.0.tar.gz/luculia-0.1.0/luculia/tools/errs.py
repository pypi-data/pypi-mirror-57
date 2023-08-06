'''
Error class definitions.
'''

class DireExists(Exception):
    '''
    An error indicating a directory already exists.
    '''

    pass

class DireNotExists(Exception):
    '''
    An error indicating a directory does not exist.
    '''

    pass

class FileExists(Exception):
    '''
    An error indicating a file already exists.
    '''

    pass

class FileNotExists(Exception):
    '''
    An error indicating a file does not exist.
    '''

    pass
