+++
title = "setuptools, setup dot pie and pip"
author = ["Thibault Lestang"]
draft = false
weight = 2003
+++

The recommended way to install a package is to use the `setuptools` library in conjunction with
`pip`, the official python _package manager_.
Effectively, this approach is roughly equivalent to copying the package to the `site-packages` directory,
expect that the process in **automated**.


## pip {#pip}

Pip is the de facto package manager for Python packages.
It's main job is to install, remove, upgrade, configure and manage Python packages, both available
locally on your machine but also hosted on on the [Python Package Index (PyPI)](https://pypi.org/).
Pip is maintained by the [Python Packaging Authority](https://www.pypa.io/en/latest/).

Installing a package with `pip` looks like this

```shell
pip install <package directory>
```

let's give it a try

```shell
# In directory analysis1/
pip install ./tstools
```

```text
ERROR: Directory './tstools' is not installable. Neither 'setup.py' nor 'pyproject.toml' found.
```

The above doesn't really look like our package got installed properly.
For `pip` to be able to install our package, we must first give it some information about it.
In fact, `pip` expects to find a python file named `setup.py` in the directory that it is
given as an argument. This file will contain some metadata about the package and tell `pip`
the location of the actual source of the package.


## `setup.py` (setup dot pie) and distribution packages {#setup-dot-py--setup-dot-pie--and-distribution-packages}

The `setup.py` file is a regular Python file that makes a call to the `setup` function
available in the `setuptools` package.

Let's have a look at a minimal `setup.py` file for our `tstools` package:

```python
from setuptools import setup

setup(name='tstools',
      version='0.1',
      description='A package to analyse timeseries',
      url='myfancywebsite.com',
      author='Spam Eggs',
      package=['tstools'],
      license='GPLv3')
```

The above gives `pip` some metadata about our package: its version, a short description,
its authors, ad its license.
In addition, it gives `setup` the location of the package to be installed, in this case
the directory `tstools`.

**IMPORTANT**: The above `setup.py` states `(...,package=["tstools"],...)`.
In English, this means "setuptools, please install the package `tstools/` located in the same directory as the file `setup.py`".
This therefore assumes that the file `setup.py` resides in the directory that _contains_ the package, in this case `analysis1/`.

```text
python-workshop/
      analysis1/
  	      data/
  	      analysis1.py
  	      setup.py
  	      tstools/
```

Actually, there are no reasons for our `tstools` package to be located in the `analysis1/` directory.
Indeed, the package is independant from this specific analysis, and we want to share it among multiple analyses.

To reflect this, let's move the `tstools` package into a new directory `tstools-dist` located next to the `anaylis1` and
`analysis2` directories:

```text
python-workshop/
      analysis1/
  	      data/
  	      analysis1.py
      analysis2/
  	      data/
  	      analysis2.py
      tsools-dist/
  	      setup.py
  	      tstools/
```

The directory `tstools-dist` is a _distribution package_, containing the `setup.py` file and the package itself - the `tstools` directory.
These are the two minimal ingredients required to _distribute_ a package, see section ??.


## Activity 3 -  Installing `tsools` with pip {#activity-3-installing-tsools-with-pip}

1.  Write a new `setup.py` file in directory `tstools-dist` including the following metadata:

    -   The name of the package (could be `tstools` but also could be anything else)
    -   The version of the package (for example 0.1)
    -   A one-line description
    -   Your name as the author
    -   Your email
    -   The GPLv3 license

    Hint: A list of optional keywords for `setuptools.setup` can be found [here](https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords).
2.  Uninstall numpy and matplotlib

    ```shell
    pip uninstall numpy matplotlib
    ```
3.  Install the `tstools` package with `pip`.
    Remember: `pip install <location of setup file>`
    Notice how `numpy` and `matplotlib` are automatically downloaded (can you find from where?)
    and installed.
4.  Move to the directory `analysis2/` and check that you can import your package from there.
    Where is this package located?
    Hint: You can check the location a package using the `__file__` attribute.
5.  The directory `analysis2` contains a timeseries under `data/`. What is the average value
    of the timeseries?

Congratulations! Your `tstools` package is now installed can be reused across your analyses...
no more dangerous copying and pasting!
