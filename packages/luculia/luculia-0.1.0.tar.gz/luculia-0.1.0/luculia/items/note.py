'''
Class definition for 'Note'.
'''

from luculia import tools

class Note:
    '''
    A plaintext note file in a Book.
    '''

    def __init__(self, path):
        '''
        Initialise the Note instance.
        '''

        self.path = str(path)
        self.name = tools.path.name(path)

    @classmethod
    def create(cls, path, body):
        '''
        Create and return a new Note.
        '''

        tools.file.create(path, body)
        return cls(path)

    def __contains__(self, text):
        '''
        Return True if the Note contains a case-insensitive substring.
        '''

        return text.lower() in self.read().lower()

    def __eq__(self, note):
        '''
        Return True if the Note is equal to another Note.
        '''

        return all([
            type(self) == type(note),
            self.path  == getattr(note, 'path', None),
        ])

    def __hash__(self):
        '''
        Return the Note's hash code.
        '''

        return hash(self.path)

    def __iter__(self):
        '''
        Yield each line in the Note's body.
        '''

        yield from self.read().splitlines(keepends=True)

    def __len__(self):
        '''
        Return the size of the Note.
        '''

        return len(self.read())

    def __repr__(self):
        '''
        Return the Note as a code-representative string.
        '''

        return f'Note({self.path!r})'

    def __str__(self):
        '''
        Return the Note as a string.
        '''

        return self.name

    def copy(self, name):
        '''
        Copy and return the Note at a new name in the same directory.
        '''

        dest = tools.file.copy(self.path, name)
        return Note(dest)

    def exists(self):
        '''
        Return True if the Note's file exists.
        '''

        return tools.file.exists(self.path)

    def read(self):
        '''
        Return the Note's body as a string.
        '''

        return tools.file.read(self.path)

    def reext(self, ext):
        '''
        Move the Note to a different extension in the same directory.
        '''

        dest = tools.file.reext(self.path, ext)
        self.__init__(dest)

    def rename(self, name):
        '''
        Move the Note to a different name in the same directory.
        '''

        dest = tools.file.rename(self.path, name)
        self.__init__(dest)

    def update(self, body):
        '''
        Update the Note with a new body.
        '''

        tools.file.update(self.path, body)
