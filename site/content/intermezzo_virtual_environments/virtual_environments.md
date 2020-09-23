+++
title = "Virtual environments"
author = ["Thibault Lestang"]
draft = false
weight = 2002
+++

Roughly speaking, the python executable `/some_dir/lib/pythonX.Y/bin/python`
and the package installation location `/some_dir/lib/pythonX.Y/site-packages/`
consitute what is commonly referred to as the _python environment_.

If you cannot install different versions of a package in a single environment,
let's have multiple environments! This is the core idea of _python virtual environments_.
Whenever a python virtual environment `my_env` is _activated_, the `python` command points to a
python executable that is unique to this environment (`my-env/lib/pythonX.Y/bin/python`), with a unique package installation location
specific to this environment (`my_env/lib/pythonX.Y/site-packages`).


## Activity 4 - Virtual environments {#activity-4-virtual-environments}

1.  Move to the `analysis1/` directory and create a virtual environment there:

    ```shell
    cd python-packaging-workshop/analysis1/
    python -m venv venv-analysis1
    ```

    This commands creates a new directory `venv-analysis1` in the current directory.
    Feel free to explore its contents.

2.  Activate the virtual envoronment for analysis1

    ```shell
    source venv-analysis1/bin/activate # GNU/Linux and MacOS
    venv-analysis1\Scripts\activate.bat # Windows command prompt
    venv-analysis1\Scripts\Activate.ps1 # Windows PowerShell
    ```

3.  What is the location of the current python executable?
    Hint: The built-in python package `sys` provides a variable `executable`.

4.  Use `pip list` to list the currently installed packages.
    Note that your package and its dependencies have disappeared, and only
    the core python packages are installed. We effectively have a "fresh" python environment.

5.  Update `pip` and install utility packages

    ```shell
    pip install --upgrade pip setuptools wheel
    ```

6.  Move to the the `tstools-dist` distribution package directory and install it into the
    current environment:

    ```shell
    pip install .
    ```

7.  Where was the package installed?
    Hint: When importing package `package` in python, use `package.__file__`
    to check the location of the corresponding `__init__.py` file.

The above exercise demonstrates that, after activating the `venv-analysis1`, the command `python`
executes the python executable `analysis1/venv-analysis1/bin/python`, and python packages are installed
in the `analysis1/venv-analysis1/lib/pythonX.Y/site-packages` directory.
This means that we are now working in a python environment that is _isolated_ from other python environments
in your machine:

-   other virtual environments
-   system python environment (see below)
-   other versions of python installed in your system
-   Anaconda environments

You can therefore install all the packages necessery to your projects, without worry of breaking
other projects.
