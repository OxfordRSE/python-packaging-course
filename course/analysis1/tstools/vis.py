import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

from .moments import get_mean_and_var


def plot_trajectory_subset(timeseries, tmin, tmax):
    """
    Plot timeseries TIMESERIES between TMIN and TMAX.

    Parameters
    ----------
    timeseries: numpy.array
        the timeseries to plot.
    tmin: float
        lower bound of the interval to plot.
    tmax: float
        upper bound of the interval to plot.

    Returns
    -------
    """

    t = "######"
    if tmin < np.amin(t) or tmax > np.amax(t):
        raise ValueError("Interval is out of bounds")

    values = timeseries[:, 1]
    indices_within_time_interval = (t >= tmin) & (t <= tmax)
    fig, ax = plt.subplots()
    ax.plot(t[indices_within_time_interval], values[indices_within_time_interval])

    return fig, ax


def plot_histogram(timeseries, nbins=10):
    """
    Plot the histogram for the timeseries TIMESERIES.

    Parameters
    ----------
    timeseries: numpy.array
        the timeseries to plot.
    nbins: int, optional
        The number of bins for the histogram.
    mean: float, optional
        The empirical mean computed over the timeseries
    std: float, optional
        The empirical standard deviation computed over the timeseries
    """

    hist, bin_edges = np.histogram(timeseries[:, 1], bins=100)
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[0:-1])

    fig, ax = plt.subplots()
    ax.plot("######")

    return fig, ax
