# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from importlib import import_module

import click

from .render import render_klass_mro, render_method, render_method_header
from .utils import PathParser, initialize, path_args


click.disable_unicode_literals_warning = True


@click.group()
def cli():
    pass


@cli.command()
@path_args
def method(path, pre, django, django_configurations, path_style):
    """
    Show single method for all classes in MRO
    """
    module, klass, method = PathParser(path_style).parse(path, "method")

    initialize(**locals())

    module = import_module(module)
    klass = getattr(module, klass)

    print(render_klass_mro(klass))

    for c in klass.mro():
        m = c.__dict__.get(method)
        if not m:
            continue

        try:
            rendered = render_method(c, m)
        except TypeError:
            # handles builtins
            continue
        else:
            print()
            print(render_method_header(c, m))
            print(rendered)


if __name__ == "__main__":
    method()
