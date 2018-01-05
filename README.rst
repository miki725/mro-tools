=========
MRO tools
=========

.. image:: https://badge.fury.io/py/mro-tools.png
    :target: http://badge.fury.io/py/mro-tools

Various cli tools related to MRO. Useful for debugging complex class strictures.

* Free software: MIT license
* GitHub: https://github.com/miki725/mro-tools

Installing
----------

You can install ``mro-tools`` using pip::

    $ pip install mro-tools

Why?
----

Inheritance is wonderful. Except when its not.
How many times did you have to debug a complex class with MRO of >30 classes?
You will then know its not pleasant.
Editors don't help much since as soon you jump to a base class, all editor
inheritance calculations are relative to the jumped class, not the original subclass.
That makes it non-trivial to see what actually happens within
code execution without dropping into ``pdb``.
This package aims to aid with such issues.
It has a collection of cli tools which help troubleshooting complex classes
with big MRO trees.

Using
-----

MRO tools exposes all tools via a single group command.
All available command can be seen by executing ``mro-tools`` command::

    ❯❯❯ mro-tools
    Usage: mro-tools [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      method  Get all method definitions within all classes...
      version  Print version of mro-tools

Each sub-command has more documentation::

    ❯❯❯ mro-tools version --help
    Usage: mro-tools version [OPTIONS]

      Print version of mro-tools

    Options:
      --help  Show this message and exit.

``mro-tools`` can also be accessed as a Python module::

    ❯❯❯ python -m mro_tools

Examples
-------

::

    ❯❯❯ python -m mro_tools method django.views.generic:FormView.get_context_data
    ========
    Full MRO
    ========
    django.views.generic.edit.FormView
    django.views.generic.base.TemplateResponseMixin
    django.views.generic.edit.BaseFormView
    django.views.generic.edit.FormMixin
    django.views.generic.base.ContextMixin
    django.views.generic.edit.ProcessFormView
    django.views.generic.base.View
    builtins.object

    ----------------------------------------------------
    django.views.generic.edit.FormMixin.get_context_data
    ----------------------------------------------------
    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super().get_context_data(**kwargs)

    -------------------------------------------------------
    django.views.generic.base.ContextMixin.get_context_data
    -------------------------------------------------------
    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs
