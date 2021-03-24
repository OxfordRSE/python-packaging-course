import matplotlib.pyplot as plt
import numpy as np
import unittest

from tstools.moments import get_mean_and_var
from tstools.vis import plot_histogram, plot_trajectory_subset


class Testtstools(unittest.TestCase):
    def setUp(self):
        self.test_timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")
        self.mean = 0.0362
        self.var = 1.0591

    def test_get_mean_and_var(self):
        mean, var = get_mean_and_var(self.test_timeseries)
        np.testing.assert_almost_equal(mean, self.mean, decimal=3)
        np.testing.assert_almost_equal(var, self.var, decimal=3)

    def test_plot_trajectory_subset(self):
        expected_pos = self.test_timeseries[:, 1][0:11]
        expected_time = self.test_timeseries[:, 0][0:11]

        fig, ax = plot_trajectory_subset(self.test_timeseries, 0, 1)
        time, pos = ax.lines[0].get_xydata().T

        np.testing.assert_equal(time, expected_time)
        np.testing.assert_equal(pos, expected_pos)

    def test_plot_histogram(self):
        fix, ax = plot_histogram(
            self.test_timeseries, nbins=100
        )
        values, hist = ax.lines[0].get_xydata().T

        hist, bin_edges = np.histogram(self.test_timeseries[:, 1], bins=100)
        bin_centers = 0.5 * (bin_edges[1:] + bin_edges[0:-1])
        fig, expected_ax = plt.subplots()
        expected_ax.plot(bin_centers, hist, "*")
        expected_values, expected_hist = expected_ax.lines[0].get_xydata().T

        np.testing.assert_equal(values, expected_values)
        np.testing.assert_equal(hist, expected_hist)


if __name__ == "__main__":
    unittest.main()
