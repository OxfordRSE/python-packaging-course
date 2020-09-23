# analysis1/analysis1.py
import numpy as np
import matplotlib.pyplot as plt
import tstools

timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")

mean, var = tstools.get_mean_and_var(timeseries)

fig, ax = tstools.plot_histogram(timeseries, nbins=100)

threshold = 3 * np.sqrt(var)
fig, ax = tstools.show_extremes(timeseries, threshold)
