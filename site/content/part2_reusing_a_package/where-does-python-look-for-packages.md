+++
title = "Where does python look for packages?"
author = ["Thibault Lestang"]
draft = false
weight = 2002
+++

When using the `import` statement, the python interpreter looks for the package (or module) in a list of directories known as the _python path_.

Let's find out about what directories make the python path:

```text
$ python
>>> import sys
>>> sys.path
['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lin-dynload', '/home/thibault/python-workshop-venv/lib/python3.8/site-packages/']
```

The order of this list matters: it is the order in which python looks into the directories that constitute the python path.
To begin with, Python first looks in the current directory.
If the package/module isn't found there, the python intepreter looks in the following directories
(in this order):

-   `/usr/lib/python38.zip`
-   `/usr/lib/python3.8`
-   `/usr/lib/python3.8/lib-dynload`

The above contain the modules and packages in the _standard library_, _i.e_ the packages and modules that come "pre-installed" with Python.
Finally, the python interpreter looks inside the directory `/home/thibault/python-workshop-venv/lib/python3.8/site-packages/`.

{{% notice note %}}
The output of `sys.path` is probaby different on your machine. It depends on many factors,
like your operating system, your version of Python, the location of your current active Python
environment.
{{% /notice %}}

For Python to find out package `tstools` it must be located in one of the directories listed in
the `sys.path` list. If it is the case, the package is said to be _installed_.

Looking back at the example in the [previous section]({{< relref "another-analysis" >}}), let's list some potential ways we can make the `tstools` package importable from the `analysis2/` directory:

1.  **Copy (`analysis1/tstools/`) in `analysis2/`**.
    You end up with two independant packages. If you make changes to one, you have to remember to make the same
    changes to the other. It's the usual copy and paste problems: inefficient and error-prone.
2.  **Add `analysis1/` to `sys.path`**.
    At the beginning of `analysis2.py`, you could just add

    ```python
    import sys
    sys.path.append("../analysis1/")
    ```

    This approach can be sufficient in some situations, but generally not recommended. What if the package directory is relocated?
3.  **Copy `analysis1/tstools` directory to the `site-packages/` directory.**
    You have to know where the `site-packages` is. This depends on your current system and python environment (see below).
    The location on your macine may very well be differnt from the location on your colleague's machine.

More generally, the three above approaches overlook a very important
point: **dependencies**.  Our package has two: numpy and matplotlib.
If you were to give your package to a colleague, nothing guarantees
that they have both packages installed.  This is a pedagogical
example, as it is likely that they would have both installed, given
the popularity of these packages.  However, if your package relies on
less widespread packages, specific versions of them or maybe a long
list of packages, it is important to make sure that they are
available.

Note that all three above approaches work.  However, unless you have a
good reason to use one of them, these are not recommended for the
reasons above. In the next section, we look at the recommended way to
install a package, using `setuptools` and `pip`.
