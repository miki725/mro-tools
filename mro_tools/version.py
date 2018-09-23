# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import sys

import click

from . import __version__, __description__


@click.group()
def cli():
    pass


@cli.command()
@click.option("-v", is_flag=True, default=False, help="Show additional information")
def version(v):
    """
    Show version of mro-tools
    """
    if v:
        print("mro tools")
        print("---------")
        print(__description__)
        print()
        print("version:", __version__)
        print("python:", sys.executable)
    else:
        print(__version__)


if __name__ == "__main__":
    version()
