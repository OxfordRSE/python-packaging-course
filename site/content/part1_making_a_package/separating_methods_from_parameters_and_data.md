+++
title = "Separating methods from parameters and data"
author = ["Thibault Lestang"]
draft = false
weight = 2001
+++

Roughly speaking, a numerical experiment is made of three components:

-   The data (dataset, or parameters of simulation).
-   The operations performed on this data.
-   The output (numbers, plots).

As we saw, scripts `analysis.py`, and `show_extremes.py` mix the three above components into a single
`.py` file, making the analysis difficult (sometimes even risky!) to modify and test.
Re-using part of the code means copying and pasting blocks of code out of their original context, which is
a dangerous practice.

In both scripts, the operations performed on the timeseries `brownian.csv` are independant from it, and could very well
be applied to another timeseries. In this workshop, we're going to extract these operations (computing the mean, the histogram, visualising the extremes...),
and formulate them as Python _functions_, grouped by theme inside _modules_, in a way that can be reused across similar analyses. We'll then bundle these modules into a Python
_package_ that will make it straightfoward to share them across different analysis, but also with other people.

A script using our package could look like this:

```python
import numpy as np
import matplotlib.pyplot as plt
import my_pkg

timeseries = np.genfromtxt("./data/my_timeseries.csv", delimiter=",")

mean, var = my_pkg.get_mean_and_var(timeseries)

fig, ax = my_pkg.get_pdf(timeseries)

threshold = 3*np.sqrt(var)
fig, ax = my_pkg.show_extremes(timeseries, threshold)
```

Compare the above to `analysis.py`: it is much shorter and easier to read.
The actual implementation of the various operations (computing the mean and variance, computing the histogram...) is now
_encapsulated_ inside the package `my_pkg`.
All that remains are the actual steps of the analysis.

If we were to make changes to the way some operations are implemented, we would simply make
changes to the package, leaving the scripts unmodified. This reduces the risk of messing of introducing errors in your analysis, when all what you want to do is modyfying
some opearation of data.
The changes are then made available to all the programs that use the package: no more copying and pasting code around.

Taking a step back, the idea of separating different components is pervasive in software developemt
and software design. Different names depending on the field (encapsulation, separation of concerns,
bounded contexts...).
