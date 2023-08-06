'''
Class definition for 'Book'.
'''

from luculia            import tools
from luculia.items.note import Note

class Book:
    '''
    A directory of plaintext Notes.
    '''

    def __init__(self, dire, ext):
        '''
        Initialise the Book instance.
        '''

        self.dire  = str(dire)
        self.ext   = str(ext)
        self.notes = {
            note.name: note for note in (
                Note(path) for path in
                tools.file.glob(self.dire, f'*.{self.ext}')
            )
        }

    def __contains__(self, name):
        '''
        Returns True if the Book contains a Note by name.
        '''

        return name in self.notes

    def __getitem__(self, name):
        '''
        Return a Note by name.
        '''

        return self.notes[name]

    def __iter__(self):
        '''
        Yield all Notes in the Book.
        '''

        yield from self.notes.values()

    def __len__(self):
        '''
        Return the number of Notes in the Book.
        '''

        return len(self.notes)

    def __repr__(self):
        '''
        Return the Book as a code-representative string.
        '''

        return f'Book({self.dire!r}, {self.ext!r})'

    def create(self, name, body):
        '''
        Create and return a new Note in the Book.
        '''

        path = tools.path.join(self.dire, f'{name}.{self.ext}')
        self.notes[name] = Note.create(path, body)
        return self.notes[name]

    def search(self, string):
        '''
        Yield all Notes in the Book containing a substring.
        '''

        for note in self:
            if string in note:
                yield note

    def sort(self, func, *, reverse=False):
        '''
        Yield all Notes in the Book in a sorted order.
        '''

        return sorted(self, key=func, reverse=reverse)
