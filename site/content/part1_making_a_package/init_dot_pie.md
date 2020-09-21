+++
title = "init dot pie"
author = ["Thibault Lestang"]
draft = false
weight = 2003
+++

Whenever you import a directory, Python will look for a file <span class="underline"><span class="underline">init</span></span>.py at the root of this
directory, and, if found, will import it.
It is the presence of this initialization file that truly makes the `tstools` directory a Python
package[^fn:1].

As a first example, let's add the following code to `__init__.py`:

```python
# tstools/__init__.py
from os.path import basename
filename = basename(__file__)
print(f"Hello from {filename}")
```

If we now import the `tstools` package:

```python
import tstools
print(tstools.filename)
```

```text
Hello from __init__.py
__init__.py
```

The lesson here is that any object (variable, function, class) defined in the `__init__.py` file is available
under the package's namespace.


## Activity 2 - Bringing all functions under a single namespace {#activity-2-bringing-all-functions-under-a-single-namespace}

Our package isn't very big, and the internal strucure with 3 different modules isnt
very relevant for a user.

**Write** the `__init__.py` so that all functions defined in
modules `tstools.py` and `show_extremes.py` are accessible directly
at the top-lvel (under the `tstools` namespace), _i.e_

```python
import tstools
mean, var = tstools.get_mean_and_var(timeseries) # instead of mean, var = tstools.moments.get_mean_and_var(...)
fig, ax = tstools.show_extremes(timeseries, 4*np.sqrt(var)) # instead of fig, ax = tstools.vis.show_extremes(...)
```

**Hint**: By default python looks for modules in the current directory
and some other locations (more about that later). When using `import`,
you can refer to modules in the current package using the _dot notation_:

```python
# import something from module that resides
# in the current package (next to the __init__.py)
from .module import something
```


## Using the package {#using-the-package}

Our package is now ready to be used in our analysis, and a analysis scripts could look like this:

```python
# analysis1/analysis1.py
import numpy as np
import matplotlib.pyplot as plt
import tstools

timeseries = np.genfromtxt("./data/my_timeseries.csv", delimiter=",")

mean, var = tstools.get_mean_and_var(timeseries)

fig, ax = tstools.get_pdf(timeseries)

threshold = 3*np.sqrt(var)
fig, ax = tstools.show_extremes(timeseries, threshold)
```

Note that the above does the job for both scripts `scripts/analysis.py` and `scripts/show_extremes.py`! Much better don't you think?

[^fn:1]: Since Python 3.3, this isn't technically true. Directories without a `__init__.py` file are called namespace packages, see [Packaging namespace packages](https://packaging.python.org/guides/packaging-namespace-packages/) on the Python Packaging User Guide). However, their discussion is beyond the scope of this course.
