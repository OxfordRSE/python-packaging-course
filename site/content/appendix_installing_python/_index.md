+++
title = "Appendix - how to install Python 3"
author = ["Thibault Lestang"]
draft = false
weight = 3001
+++

## Install Python 3 through Anaconda/Miniconda

There are may ways of installing Python 3, depending on your operating
system, but also what you want to use Python for.  Perhaps the most
straightforward way to install a "ready to go" Python is to install
[Anaconda](https://www.anaconda.com/). You can view Anaconda as a
bundle including Python itself + useful utilities (such as the `pip`
package manager) + several gigabytes worth of Python packages.  An
alternative to Anaconda is
[Miniconda](https://docs.conda.io/en/latest/miniconda.html), which is
essentially a stripped version of Anaconda.  It provides a lighter
Python distribution consisting of just Python + a handful of core
utility packages.

For the purpose of this course, it really doesn't matter if you
install Miniconda or Anaconda. it you'd rather save some disk
space and go for a shorter download, we recommend you go for
Miniconda.

-   Click
    [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html##regular-installation)
    for instructions on how to install Miniconda/Anaconda.

If you'd rather install Python outside of Anaconda or Miniconda,
check out our instructions on how to install Python.

If you encounter issues whilst installing any of the above, feel free
to get in touch by [opening an
issue](https://docs.github.com/en/enterprise/2.15/user/articles/creating-an-issue)
on [the course repository](https://github.com/OxfordRSE/python-packaging-course).

## Install Python 3 (outside of Anaconda/Miniconda)

### GNU/Linux

On most GNU/Linux distributions, the command `python` points to 
the system's Python 2 interpreter.
Instead, Python 3 is often available as the `python3` package (and the
`python3` command).

On Ubuntu/Debian (and probably Linux Mint), you can install Python 3, the `pip` package manager
and the `venv` module using the `apt` package manager:

    sudo apt install python3 python3-pip python3-venv

On Fedora, Python 3 should already be there. In case it's not, you can install it
with

    sudo dnf python3

This should include `pip` and the `venv` module.

Be sure to check your installation by opening a terminal and running ~python --version~.


<a id="orgb5ad19b"></a>

### MacOS

1.  Install homebrew (see the [installation instructions](https://brew.sh/)).
2.  Install Python 3

    brew install python3

That's it. Be sure to check your installation by opening a terminal and running ~python --version~.

<a id="org6d40136"></a>

### Windows

1.  Download the installer for the latest stable version of python [here](https://www.python.org/downloads/windows/).
    (Most likely the *Windows x86-64 executable installer*).
2.  Execute the Python installer - **be sure to tick** *Add Python 3.8 to PATH*.

Be sure to check your installation by opening a command prompt and typing ~python --version~.
