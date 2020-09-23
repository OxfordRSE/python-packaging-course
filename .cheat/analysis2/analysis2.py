# analysis2/analysis2.py
import sys
import numpy as np

sys.path.append("../analysis1/")

import tstools

timeseries = np.genfromtxt("./data/data_analysis2.csv", delimiter=",")
fig, ax = tstools.plot_trajectory_subset(timeseries, 0, 50)
