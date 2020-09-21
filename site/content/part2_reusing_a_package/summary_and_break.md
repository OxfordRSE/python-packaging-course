+++
title = "Summary and break"
author = ["Thibault Lestang"]
draft = false
weight = 2005
+++

-   In order to reuse our package across different analyses, we must _install_ it.
    In effect, this means copying the package into a directory that is in the python path.
    This shouldn't be done manually, but instead using the `setuptools` package to write a
    `setup.py` file that is then processed by the `pip install` command.
-   It would be both cumbersome and error-prone to have to reinstall the package each time
    we make a change to it (to fix a bug for instance). Instead, the package can be installed
    in "editable" mode using the `pip install -e` command. This just redirects the python
    interpreter to your project directory.
-   The main value of packaging software is to faciliate its reuse across different projects.
    One you have extracted the right operations into a package that is independant of your
    analysis, you can easily "share" it between projects. In this way you avoid innefficient
    and dangerous duplication of code.

Beyond greatly facilitating code reuse, writing a python package (as opposed to a loosely
organised collection of modules) enables a clear organisation of your software into modules
and possibly subpackages. It makes it much easier for others, as well as yourself, to
understand the structure of your software, _i.e_ what-does-what.

Moreover, organising your python software into a package gives you access to a myriad
of fantastic tools used by thousands of python developers everyday. Examples include
pytest for automated testing, sphinx for building you documentation, tox for automation
of project-level tasks.

Next, we'll talk about python virtual environments. But before, fancy a little break?

{{< figure src="/kisspng-cafe-coffee-cup-tea-cafe-graphic-5ac8dcf5aa0815.5906502615231132056965.png" >}}
