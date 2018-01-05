# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import click

from . import __version__


@click.group()
def cli():
    pass


@cli.command()
def version():
    """
    Print version of mro-tools
    """
    print(__version__)


if __name__ == '__main__':
    version()
