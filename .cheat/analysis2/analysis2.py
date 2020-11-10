# analysis2/analysis2.py
import matplotlib.pyplot as plt
import numpy as np

import tstools

timeseries = np.genfromtxt("./data/hotwire.csv", delimiter=",")
fig, ax = tstools.plot_trajectory_subset(timeseries, 0, 0.25)

ax.set_ylabel("$u_x(t)$ (m/s)", fontsize=16)
ax.set_xlabel("$t$ (s)", fontsize=16)

ax.plot()
plt.show()
