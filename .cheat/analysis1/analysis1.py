# analysis1/analysis1.py
import numpy as np
import matplotlib.pyplot as plt

import tstools.moments
import tstools.vis
import tstools.extremes

timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")

mean, var = tstools.moments.get_mean_and_var(timeseries)

fig1, ax1 = tstools.vis.plot_histogram(timeseries, nbins=100)

threshold = 3 * np.sqrt(var)
fig2, ax2 = tstools.extremes.show_extremes(timeseries, threshold)

ax1.plot()
ax2.plot()

plt.show()
