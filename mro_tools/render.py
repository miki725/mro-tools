# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import inspect

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer


def add_indent(s, indent):
    return "\n".join(" " * indent + i for i in s.splitlines())


def render_klass_mro(klass, indent=0):
    return add_indent(
        "\n".join(
            ["========", "Full MRO", "========"]
            + ["{}.{}".format(c.__module__, c.__name__) for c in klass.mro()]
        ),
        indent,
    )


def render_klass_header(klass, indent=0):
    header = "{}.{}".format(klass.__module__, klass.__name__)

    return add_indent("\n".join(["=" * len(header), header, "=" * len(header)]), indent)


def render_method_header(klass, method, indent=0):
    header = "{}.{}.{}".format(klass.__module__, klass.__name__, method.__name__)

    return add_indent("\n".join(["-" * len(header), header, "-" * len(header)]), indent)


def render_klass(klass, indent=0):
    source = inspect.getsource(klass)
    lines = source.splitlines()
    _indent = len(lines[0]) - len(lines[0].lstrip(" \t"))
    lines = [i[_indent:] for i in lines]

    return add_indent(
        highlight("\n".join(lines), PythonLexer(), TerminalFormatter()), indent
    )


def render_method(klass, method, indent=0):
    source = inspect.getsource(method)
    lines = source.splitlines()
    _indent = len(lines[0]) - len(lines[0].lstrip(" \t"))
    lines = [i[_indent:] for i in lines]

    return add_indent(
        highlight("\n".join(lines), PythonLexer(), TerminalFormatter()), indent
    )
