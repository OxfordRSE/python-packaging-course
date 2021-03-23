+++
title = "Another analysis"
author = ["Thibault Lestang"]
draft = false
weight = 2001
+++

Let's say that we have another directory `analysis2`, that contains another
but similar dataset to `analysis1/data/brownian.csv`.
Now that we've structured our software into a python package, we would like
to reuse that package for our second analysis.

In the directory `analysis2/`, let's write a script `analysis2.py`, that imports the `tstools` package created in the previous section.

```text
analysis2/
      analysis2.py
      data/
  	      hotwire.csv
```

```python
# analysis2/analysis2.py
import numpy as np

import tstools

timeseries = np.genfromtxt("./data/hotwire.csv", delimiter=",")
fig, ax = tstools.plot_trajectory_subset(timeseries, 0, 50)
```

```text
$ python analysis2.py
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
  File "<stdin>", line 5, in main
ModuleNotFoundError: No module named 'tstools'
```

At the moment lives in the directory `analysis1/`, and, unfortunately, Python cannot find it!
How can we tell Python where our package is?
