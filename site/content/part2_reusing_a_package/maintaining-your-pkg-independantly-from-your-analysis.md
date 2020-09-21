+++
title = "Maintaining your package indepently from the anaylises that use it"
author = ["Thibault Lestang"]
draft = false
weight = 2004
+++

In the previous section you made your package "pip installable" by creating a `setup.py` file.
You then installed the package, effectively making accessible between different analysis directories.

However, a package is never set in stone: as you work on your analyses, you will almost certainly likely make changes to it,
for instance to add functionalities or to fix bugs.

You could just reinstall the package each time you make a modification to it, but this
obviously becomes tedious if you are constantly making changes (maybe to hunt down a bug) and/or testing your package.
In addition, you may simply forget to reinstall your package, leading to potentially very frustrating and time-consuming errors.


## Editable installs {#editable-installs}

`pip` has the ability to install the package in a so-called "editable" mode.
Instead of copying your package to the package installation location, pip will just
write a link to your package directory.
In this way, when importing your package, the python interpreter is redirected to
your package project directory.

To install your package in editable mode, use the `-e` option for the `install` command:

```shell
pip install -e .
```


## Actvity 4 - Editable install {#actvity-4-editable-install}

1.  Uninstall the package with `pip uninstall tstools`
2.  List all the installed packages and check that `tstools` is not among them
    Hint: Use `pip --help` to get alist of available `pip` commands.
3.  re-install `tstools` in editable mode.
4.  Modify the `tstools.vis.plot_trajectory_subset` so that it returns the maximum value
    over the trajectory subset, in addition to the `figure` and `axis`.
    Hint: You can use the numpy function `amax` to find the maximum of an array.
5.  What is the maximum value of the timeseries in `analysis1/data/timeseries1.csv` between
    t=0 and t = 4 ?

In editable mode, `pip install` just write a file `<package-name>.egg-link` at the package
installation location in place of the actual package. This file contains the location of the
package in your package project directory:

```shell
cat ~/python-workshop-venv/lib/python3.8/site-packages/tstools.egg-link
/home/thibault/python-packaging-workshop/tstools
```
