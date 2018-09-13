# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import inspect
from importlib import import_module

import click
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer


click.disable_unicode_literals_warning = True


def parse_dot(path):
    module, klass_and_method = path.split(':')
    klass, method = klass_and_method.split('.')
    return module, klass, method


def parse_pycharm(path):
    module_and_klass, method = path.split('#')
    module, klass = module_and_klass.rsplit('.', 1)
    return module, klass, method


parse_mapping = {
    'dot': parse_dot,
    'pycharm': parse_pycharm,
}


def print_method(klass, method):
    source = inspect.getsource(method)
    lines = source.splitlines()
    indent = len(lines[0]) - len(lines[0].lstrip(' \t'))
    lines = [i[indent:] for i in lines]

    header = '{}.{}.{}'.format(
        klass.__module__,
        klass.__name__,
        method.__name__,
    )

    print('-' * len(header))
    print(header)
    print('-' * len(header))
    print(highlight('\n'.join(lines), PythonLexer(), TerminalFormatter()))


@click.group()
def cli():
    pass


@cli.command()
@click.argument(
    'path',
    metavar='METHOD_PATH',
)
@click.option(
    '--pre',
    metavar='CODE',
    help="""
    Arbitrary python statements to exec before importing module.
    """
)
@click.option(
    '--django',
    is_flag=True,
    default=False,
    help="""
    Initialize django before importing modules.
    """
)
@click.option(
    '--django-configurations',
    is_flag=True,
    default=False,
    help="""
    Initialize django before importing modules by using django-configurations.
    """
)
@click.option(
    '--path-style',
    default='dot',
    type=click.Choice(['dot', 'pycharm']),
    help="""
    Style in which path is provided.
    * dot - standard dot-notation (e.g. "module.path:Class.method")
    * pycharm - PyCharm notation (e.g. "module.path.Class#method")
    """
)
def method(path, pre, django, django_configurations, path_style):
    """
    Get all method definitions within all classes within MRO
    """
    module, klass, method = parse_mapping[path_style](path)

    if django:
        import django
        django.setup()

    if django_configurations:
        import configurations
        configurations.setup()

    if pre:
        exec(pre)

    module = import_module(module)
    klass = getattr(module, klass)

    print('========')
    print('Full MRO')
    print('========')
    for c in klass.mro():
        print('{}.{}'.format(c.__module__, c.__name__))

    for c in klass.mro():
        m = c.__dict__.get(method)
        if not m:
            continue

        try:
            print()
            print_method(c, m)
        except TypeError:
            # handles builtins
            continue


if __name__ == '__main__':
    method()
