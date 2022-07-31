import click
import sys
from classmodule import note
from tnote.module import edit, delete, move, view, index, get_notes


@click.command()
@click.argument("name", required=False)
@click.option('--recent', '-r', is_flag=True, show_default=True, default=False, help='Opens most recent note')
@click.option("--edit", "-e", 'action', flag_value='edit', show_default=True, default='edit')
@click.option("--move", "-m", 'action', flag_value='move', show_default=True, default='edit')
@click.option("--view", "-v", 'action', flag_value='view', show_default=True, default='edit')
@click.option("--del", "-d", 'action', flag_value='del', show_default=True, default='edit')
@click.option('--path', '-p', 'path', type=click.Path())
def cli(name, action, path, recent):
    if recent:
        name = ".recent"
    if name == None:
        index()
        return
    match action:
        case 'edit':
            if path is None:
                edit(name)
            else:
                edit(name, path)
        case 'del':
            delete(name)
        case 'move':
            if path is None:
                print('Error: Must use -p to provide a path that the file be moved to')
            else:
                move(name, path)
        case 'view':
            view(name)


if __name__ == '__main__':
    cli()
