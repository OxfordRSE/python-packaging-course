+++
title = "The tstools package"
author = ["Thibault Lestang"]
draft = false
weight = 2002
+++

We now have a `tstools` directory with 3 modules:

```text
analysis1/
      tstools/
  	      __init__.py
  	      moments.py
  	      vis.py
  	      show_extremes.py
      data/
```

In a way, the directory `tstools` is already a package, in the sense that it is possible to import functions from the modules:

```python
import numpy as np

import tstools.moments
from tstools.vis import plot_histogram

timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")

mean, var = tstools.moments.get_mean_and_var(timeseries)
fig, ax = tstools.vis.plot_histogram(timeseries)
```

Let's try to import the package as a whole:

```python
# compute-mean.py
import numpy as np

import tstools

timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")

mean = tstools.moments.get_mean_and_var(timeseries)
```

```text
$ python compute_mean.py
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
AttributeError: module 'tstools' has no attribute 'moments'
```

What happened here?
{{% notice info %}}
When importing the directory `tstools`, the python interpreter
looks for a file named `__init__.py` inside this directory and imports this python file.
If this python file is empty, or simply doesnt exists... nothing is imported.
{{% /notice %}}

In the following section we add some `import` statements into the `__init__.py` so that
all our functions (in the three modules) ar available under the single namespae `tstools`.
