+++
title = "From scripts to modules"
author = ["Thibault Lestang"]
draft = false
weight = 2001
+++

## Functions, modules, packages {#functions-modules-packages}

-   functions, classes

<!--listend-->

```python
# operations.py
def add(a,b):
    return a+b
```

-   modules
    Collection of python objects (classes, functions, variables)

<!--listend-->

```python
from operations import add
# "From file (or module) operations.py import object add"

result = add(1,2)
```

-   packages
    Collection of modules (`.py` files)

<!--listend-->

```python
from calculator.operations import add
from calculator.representations import hexa

a = hexa(1)
b = hexa(2)

result = add(a,b)
```


## Activity 1 - Turning scripts into a collection of functions {#activity-1-turning-scripts-into-a-collection-of-functions}

Let's rewrite both scripts `scripts/analysis.py` and `scripts/show_extremes.py`
as a collection of functions that can be reused in separate scripts.

The directory `analysis1/tstools/` contains 3 python modules that contain (incomplete) functions performing
the same operations on data described in the original scripts `analysis.py` and `show_extremes.py`:

```text
python-packaging-workshop/
      scripts/
      analysis1/
  	      tstools/
  		      __init__.py
  		      moments.py
  		      vis.py
  		      extremes.py
```

1.  Open `moments.py` and complete function `get_mean_and_var` (replace the
    string `"######"`).
2.  Open file `vis.py` and complete functions `plot_trajectory_subset` and
    `plot_histogram` (replace the strings `"######"`).

{{% notice tip %}}
Use `scripts/analysis.py` as a reference.
{{% /notice %}}

{{% notice tip %}}
You can run the test script `tests.py` in `analysis1/` to test that everything is working fine.
{{% /notice %}}

The file `tstools/extremes.py` implements a function `show_extremes` corresponding to script `show_extremes.py`.
It is already complete.
