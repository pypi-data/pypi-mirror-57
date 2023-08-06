'''
Click command 'list'.
'''

import click

from luculia.comms.base import group

@group.command()
@click.pass_obj
def list(obj):
    '''
    List all notes.
    '''

    for note in obj.book:
        click.echo(note)
    click.echo()
