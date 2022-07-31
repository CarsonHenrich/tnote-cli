import os
from textwrap import indent
from rich.console import Console
from rich.markdown import Markdown
import click
import json
import sys

DATAPATH = os.path.expanduser('~/.tnotes/')
NOTESPATH = os.path.join(DATAPATH, "notes")
CONFIGPATH = os.path.expanduser('~/.tnote.json')
INDEXPATH = os.path.join(DATAPATH, "index.json")
EDITOR = os.getenv("$EDITOR")
RECENT = '.recent'

console = Console()


def edit(name, path=NOTESPATH):
    intialize_files()
    index_dict = get_index()

    try:
        note = index_dict[name]
        path = note["path"]
    except (UnboundLocalError, KeyError):
        if name == RECENT:
            print("No recent note exists")
            return
        else:
            path = os.path.join(path, name+'.md')
    note_dict = {"name": name, "path": path}
    with open(INDEXPATH, 'w') as index_file:
        if not os.path.exists(path):
            f = open(path, 'x')
            f.close
            try:
                note["path"]
            except (KeyError, UnboundLocalError):

                index_dict.update({name: note_dict})
        if name != RECENT:
            index_dict[RECENT] = note_dict
        json.dump(index_dict, index_file)
    click.edit(filename=path, editor=EDITOR)


def view(name):
    intialize_files()
    os.system('clear -x')
    index_dict = get_index()
    with open(index_dict[name]['path'], 'r+') as note:
        console.print(Markdown(note.read()))
    if name != RECENT:
        index_dict[RECENT] = index_dict[name]
    write_index(index_dict)


def delete(name):
    intialize_files()
    index_dict = get_index()
    os.remove(index_dict[name]['path'])
    index_dict.pop(name)
    write_index(index_dict)


def move(name, topath):
    intialize_files()
    dir_name, file_name = os.path.split(topath)
    new_name, temp = file_name.split('.')
    index_dict = get_index()
    note = index_dict[name]
    os.rename(note['path'], topath)
    if new_name != name:
        note['name'] = new_name
    note['path'] = topath
    index_dict[new_name] = index_dict.pop(name)
    write_index(index_dict)


def index():
    intialize_files()
    index_dict = get_index()
    print("--------------------INDEX--------------------")
    keys = index_dict.keys()
    for note in keys:
        print("\
------------------------------------------------------\n\
Note ID: {}\n\
Name: {}\n\
Path: {}\n\
------------------------------------------------------\n".format(note, index_dict[note]['name'], index_dict[note]['path']))


def intialize_files():
    if not os.path.exists(CONFIGPATH):
        open(CONFIGPATH, "x")
    if not os.path.exists(DATAPATH):
        os.mkdir(DATAPATH)
    if not os.path.exists(NOTESPATH):
        os.mkdir(NOTESPATH)
    if not os.path.exists(INDEXPATH):
        index = open(INDEXPATH, 'w')
        index.write('{\n\n}')
        index.close()


def get_index(name=None):
    index_dict = {}
    with open(INDEXPATH, 'r') as index_file:
        index_dict = json.load(index_file)
        try:
            return index_dict[name]
        except KeyError:
            return index_dict


def write_index(dict: dict):
    with open(INDEXPATH, 'w') as index:
        json.dump(dict, index)
