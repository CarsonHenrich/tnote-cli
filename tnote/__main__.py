
import click
import sys
#from tnote.classmodule import MyClass
#from tnote.funcmodule import my_function


@click.command()
@click.argument('name')
def main(name):
    print('passed argument :: {}'.format(name))

    """
    my_function('hello world')
    my_object = MyClass('Thomas')
    my_object.say_name()
    """


if __name__ == '__main__':
    main()
