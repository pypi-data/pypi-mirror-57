'''
Click command base group.
'''

from collections import namedtuple

import click

from luculia.items import Book
from luculia       import tools

Object = namedtuple('Object', ['book', 'conf'])

@click.group()
@click.pass_context
def group(context):
    '''
    Luculia: the personal note-taking engine.
    '''

    if not context.obj:
        conf = tools.conf.parse()
        book = Book(conf['directory'], conf['extension'])
        context.obj = Object(book, conf)
