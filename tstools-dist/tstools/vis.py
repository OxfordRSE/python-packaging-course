import matplotlib.pyplot as plt
import numpy as np
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

    t = timeseries[:,0]
    if tmin < np.amin(t) or tmax > np.amax(t):
        raise ValueError("Interval is out of bounds")

    values = timeseries[:,1]
    indices_within_time_interval = (t >= tmin) & (t <= tmax)
    fig, ax = plt.subplots()
    ax.plot(
        t[indices_within_time_interval], values[indices_within_time_interval]
    )

    return fig, ax


def plot_histogram(timeseries, nbins=10, mean=None, std=None):
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

    def get_theoritical_histogram(fluct_min, fluct_max, std, mean, nbins=100):
        bin_edges = np.linspace(fluct_min, fluct_max, nbins + 1)
        nb_samples = len(timeseries[:, 1])
        rescaled_bin_edges = (bin_edges - mean) / (std * np.sqrt(2))
        hist = (
            0.5
            * nb_samples
            * (erf(rescaled_bin_edges[1:]) - erf(rescaled_bin_edges[:-1]))
        )
        return hist, bin_edges

    hist, bin_edges = np.histogram(timeseries[:, 1], bins=100)
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[0:-1])

    fig, ax = plt.subplots()
    ax.plot(bin_centers, hist, "*")

    if (not std) or (not mean):
        mean, var = get_mean_and_var(timeseries)
        std = np.sqrt(var)
    hist, bin_edges = get_theoritical_histogram(
        np.amin(bin_edges), np.amax(bin_edges), std, mean
    )
    ax.plot(bin_centers, hist)

    return fig, ax
