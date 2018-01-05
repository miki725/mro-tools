# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import click

from .method import cli as method_cli
from .version import cli as version_cli


cli = click.CommandCollection(sources=[
    method_cli,
    version_cli,
])


if __name__ == '__main__':
    cli()
