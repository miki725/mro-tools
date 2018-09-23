# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import click


def path_args(f):
    wrappers = [
        click.argument("path", metavar="METHOD_PATH"),
        click.option(
            "--pre",
            metavar="CODE",
            help="Arbitrary python statements to exec before importing module.",
        ),
        click.option(
            "--django",
            is_flag=True,
            default=False,
            help="Initialize django before importing modules.",
        ),
        click.option(
            "--django-configurations",
            is_flag=True,
            default=False,
            help="Initialize django before importing modules by using django-configurations.",
        ),
        click.option(
            "--path-style",
            default="dot",
            type=click.Choice(["dot", "pycharm"]),
            help=(
                "Style in which path is provided.\n"
                '* dot - standard dot-notation (e.g. "module.path:Class.method")\n'
                '* pycharm - PyCharm notation (e.g. "module.path.Class#method")'
            ),
        ),
    ]

    for w in wrappers[::-1]:
        f = w(f)

    return f


def initialize(pre, django, django_configurations, **kwargs):
    if django:
        import django

        django.setup()

    if django_configurations:
        import configurations

        configurations.setup()

    if pre:
        exec(pre)


class PathParser(object):
    def __init__(self, style):
        self.style = style

    def method_dot(self, path):
        module, klass_and_method = path.split(":")
        klass, method = klass_and_method.split(".")
        return module, klass, method

    def method_pycharm(self, path):
        module_and_klass, method = path.split("#")
        module, klass = module_and_klass.rsplit(".", 1)
        return module, klass, method

    def klass_dot(self, path):
        module, klass = path.split(":")
        return module, klass

    def klass_pycharm(self, path):
        module, klass = path.rsplit(".", 1)
        return module, klass

    def parse(self, path, type="method"):
        return getattr(self, "{}_{}".format(type, self.style))(path)
