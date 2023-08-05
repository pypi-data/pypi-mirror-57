``termcolor_util`` is a set of functions on top of termcolor for every
single color.

Installation
============

.. code:: sh

    pip install termcolor_util

Functions
=========

.. code:: python

    def yellow(text: str, bold=False, underline=False) -> str: ...

    def green(text: str, bold=False, underline=False) -> str: ...

    def blue(text: str, bold=False, underline=False) -> str: ...

    def red(text: str, bold=False, underline=False) -> str: ...

    def gray(text: str, bold=False, underline=False) -> str: ...

    def cyan(text: str, bold=False, underline=False) -> str: ...

    def magenta(text: str, bold=False, underline=False) -> str: ...

    def white(text: str, bold=False, underline=False) -> str: ...

Beside colors, there is a function for directly printing on the stderr.

.. code:: python

    def eprint(*args) -> None: ...
