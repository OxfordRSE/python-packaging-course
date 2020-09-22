+++
title = "Building python distributions"
author = ["Thibault Lestang"]
draft = false
weight = 2001
+++

Before you can distribute a package, you must first create a _distribution_.
A distribution is a single file that bundles all the files and data necessary to install and use
the package - but also sometimes compile and test it.

A distribution usually takes the from of an archive (`.tar`, `.zip` or similar).
There are several possible distribution formats, but in 2020, only two are really important: the _source distribution_ (sdist) and the _wheel_ (bdist\_wheel).


## Source distributions {#source-distributions}

Python distributions are commonly built using the `setuptools` library, _via_ the `setup.py` file.
Building a source distribution looks like this:

```shell
python setup.py sdist
```

```text
running sdist
running egg_info
writing tstools.egg-info/PKG-INFO
writing dependency_links to tstools.egg-info/dependency_links.txt
writing requirements to tstools.egg-info/requires.txt
writing top-level names to tstools.egg-info/top_level.txt
reading manifest file 'tstools.egg-info/SOURCES.txt'
writing manifest file 'tstools.egg-info/SOURCES.txt'
running check
creating tstools-0.1
creating tstools-0.1/tstools
creating tstools-0.1/tstools.egg-info
copying files to tstools-0.1...
copying setup.py -> tstools-0.1
copying tstools/__init__.py -> tstools-0.1/tstools
copying tstools/show_extremes.py -> tstools-0.1/tstools
copying tstools/tstools.py -> tstools-0.1/tstools
copying tstools.egg-info/PKG-INFO -> tstools-0.1/tstools.egg-info
copying tstools.egg-info/SOURCES.txt -> tstools-0.1/tstools.egg-info
copying tstools.egg-info/dependency_links.txt -> tstools-0.1/tstools.egg-info
copying tstools.egg-info/requires.txt -> tstools-0.1/tstools.egg-info
copying tstools.egg-info/top_level.txt -> tstools-0.1/tstools.egg-info
Writing tstools-0.1/setup.cfg
creating dist
Creating tar archive
removing 'tstools-0.1' (and everything under it)
```

This mainly does three things:

-   It gathers the python source files that consitute the package (incuding the `setup.py`).
-   It writes some metadata about the package in a directory `<package name>.egg-info`.
-   It bundles everyting into a tar archive.

The newly created sdist is written in a directory `dist` next to the `setup.py` file:

```shell
tar --list -f dist/tstools-0.1.tar.gz
```

```text
tstools-0.1/
tstools-0.1/PKG-INFO
tstools-0.1/setup.cfg
tstools-0.1/setup.py
tstools-0.1/tstools/
tstools-0.1/tstools/__init__.py
tstools-0.1/tstools/show_extremes.py
tstools-0.1/tstools/tstools.py
tstools-0.1/tstools.egg-info/
tstools-0.1/tstools.egg-info/PKG-INFO
tstools-0.1/tstools.egg-info/SOURCES.txt
tstools-0.1/tstools.egg-info/dependency_links.txt
tstools-0.1/tstools.egg-info/requires.txt
tstools-0.1/tstools.egg-info/top_level.txt
```

> Take a moment to explore the content of the archive.

As the name suggest a source distribution is nothing more than the source code of your package,
along with the `setup.py` necessary to install it.
Anyone with the source distribution therefore has everything they need to install your package.
Actually it's even possible to give the sdist directly to `pip`:

```shell
pip install tstools-0.1.tar.gz
```

And you're done!


## Wheel distributions {#wheel-distributions}

Source distributions are very basic, and installing them basically amount
to running the package's `setup.py` script.
These poses two issues:

-   In addition to the call to `setup`, the `setup.py` can contain any valid Python.
    Thinking about security for moment, this means that installing a package could
    result in the execution of malicious code.
-   To install from a source distribution, `pip` must first unpack the distribution, then
    execute the `setup.py` script. Directly unpacking to the correct location in the python
    path would be much faster.
-   Package can contain code written in a compiled language like C or Fortran. Source
    distributions assume that the recipient has all the tools necesseray to compile
    this code. Compiling code can also takes time (hours!).

This issues can be overcome by using _wheel distributions_.
For pure-Python packages, a wheel is very similar to a source distribution: it's an
archive that contains both the python source of the package and some metadata.
The main difference with sdists is that **wheels doesn't require pip to execute
the `setup.py`** file, instead the content of wheels is directly unpacked in the correct
location - most likely your current environment's `site-packages/` directory.
This makes the installation of wheels both safer and faster.

> Another very important feature of python wheels is that they can embed compiled code,
> effectively alleviating the need for the recipient to compile (_build_) anything.
> As a result, the wheel is platform-dependant, but makes the installation considerably easier
> and faster. For this reason, wheels are part of the family of _built distrubtions_.
> Another type of built distribution is the python _egg_. However, the wheel format was
> created in response to the shortcomings of Python eggs and this format is now obsolete.
> See [Wheel vs Egg](https://packaging.python.org/discussions/wheel-vs-egg/) on the Python Packaging User Guide.


### Activity 6 - Building a Python wheel {#activity-6-building-a-python-wheel}

1.  Create a new virtual environment for this activity

    ```shell
    python -m venv test-wheel
    source test-wheel/bin/activate # (GNU/Linux and MacOS)
    test-wheel\Scripts\activate.bat # (Windows)
    ```
2.  Build a wheel

    ```shell
    python setup.py bdist_wheel
    ```
3.  Install the wheel using `pip`.
    Hint: wheels are written in the `dist/` directory, next to the `setup.pt` file, just
    like source distributions.
