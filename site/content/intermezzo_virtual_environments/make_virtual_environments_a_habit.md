+++
title = "Make virtual environments a habit"
author = ["Thibault Lestang"]
draft = false
weight = 2003
+++

You just learned what are python virtual environment and how to use them? Don't look back, and make them a habit.
The limitation that only one version of a package can be installed at one time in one python environment can be the source
of very frustrating problems, distracting you from your research.
Moreover, using one python environment for all your projects means that this environment will change as you work on different projects,
making it very hard to resolve dependency problems when they (and they will) occur.

Most of the time, a better approach is to have one (or more if needed) virtual environments per analyses and projects.
Coming back to our earlier example with the `tstools` package used in analysis analysis1 and analysis2, a recommended setup
would be

```text
tstools/
      setup.py
      tstools
      venv-tstools
(venv-tstools) $ pip install -e tstools/

analysis1/
      analysis1.py
      data/
      venv-analysis1/
(venv-analysis1) $ pip install tstools/

analysis2/
      analysis2.py
      data/
      venv-analysis2/
(venv-analysis2) $ pip install tstools/
```

When working on the package itself, we work within the virtual environment `venv-tstools`, in
which the package is installed in editable mode. In this way, we avoid constant re-installation
of the package each time we make a change to it.

When working on either analyses, we activate the corresponding virtual environment, in which
our package `tstools` is installed in normal, non-editable mode, possibly along all the
other packages that we need for this particular analysis.

> Most GNU/Linux distributions as well as MacOS come with a version of python already installed.
> This version is often referred to as the _system python_ or the _base python_. **Leave it alone**.
> As the name suggest, this version of python is used likely to be used by some parts of your system,
> and updating or breaking it would mean breaking these partsof your system that rely on it.
