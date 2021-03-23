# analysis1/analysis1.py
import numpy as np
import matplotlib.pyplot as plt

import tstools.moments
import tstools.vis

timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")

mean, var = tstools.moments.get_mean_and_var(timeseries)

fig, ax = tstools.vis.plot_histogram(timeseries, nbins=100)

ax.plot()

plt.show()
