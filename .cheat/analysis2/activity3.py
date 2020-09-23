import numpy as np

import tstools

timeseries = np.genfromtxt("./data/data_analysis2.csv", delimiter=",")
fig, ax, maxvalue = tstools.plot_trajectory_subset(timeseries, 0, 4)
print(f"The maximum value is {maxvalue}")
