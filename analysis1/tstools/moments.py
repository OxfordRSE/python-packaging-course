import numpy as np


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

    return np.mean(timeseries[:, 1]), "######"
