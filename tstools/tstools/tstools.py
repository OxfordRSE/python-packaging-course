import numpy as np
import matplotlib.pyplot as plt

def get_mean_and_var(timeseries):
    """
    Compute and return the average (empirical mean) and empirical variance
    over TIMESERIES.

    Parameters
    ----------
    timeseries: numpy.array
        The timeseries

    Returns
    -------
    mean, var: float
        A tuple which first element is the mean and second the variance.
    """

    return np.mean(timeseries), np.var(timeseries)

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
    if (tmin < np.amin(t) or tmax > np.amax(t)):
        raise ValueError("Interval is out of bounds")

    indices_within_time_interval = (t>=tmin) & (t<=tmax)

    values = timeseries[:,1]
    return plt.plot(t[indices_within_time_interval], values[indices_within_time_interval])

def plot_histogram(timseries, nbins=10, mean=None, std=None):
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

    hist, bin_edges = np.histogram(timeseries[:,1], bins=nbins)
    bin_centers = 0.5*(bin_edges[1:]+bin_edges[0:-1])

    plot_histogram = plt.plot(bin_centers, hist, "*")

    # Plot gaussian distribution
    if (not std) or (not mean):
        mean, std = get_mean_and_var(timeseries)        
    std_inverse = 1./std
    normalisation = std_inverse/np.sqrt(2.0*np.pi)
    gaussian = lambda x : normalisation*np.exp(-(x-mean)*(x-mean)*0.5*std_inverse)
    fluctuation_domain = np.linspace(min(bin_centers),max(bin_centers),100)
    plot_gaussian = plt.plot(fluctuation_domain, gaussian(fluctuation_domain))

    return plot_histogram, plot_gaussian
