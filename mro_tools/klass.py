# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from importlib import import_module

import click

from .render import render_klass, render_klass_header, render_klass_mro
from .utils import PathParser, initialize, path_args


click.disable_unicode_literals_warning = True


@click.group()
def cli():
    pass


@cli.command()
@path_args
@click.option(
    "--all",
    is_flag=True,
    default=False,
    help="Show complete class definition for all classes in MRO",
)
def klass(path, pre, django, django_configurations, path_style, all):
    """
    Show MRO for class
    """
    module, klass = PathParser(path_style).parse(path, "klass")

    initialize(**locals())

    module = import_module(module)
    klass = getattr(module, klass)

    print(render_klass_mro(klass))

    if all:
        for c in klass.mro():
            try:
                rendered = render_klass(c, 4)
            except TypeError:
                pass
            else:
                print()
                print(render_klass_header(c))
                print(rendered)


if __name__ == "__main__":
    klass()
