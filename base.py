import numpy as np
import matplotlib.pyplot as plt

timeseries = np.genfromtxt("./data/brownian.csv", delimiter=",")

# Compute and print mean and standard deviation
mean = np.mean(timeseries[:,1])
std = np.std(timeseries[:,1])
print(f"The mean is {mean}")
print(f"The standard deviation is {std}")

# Plot trajectory between tmin=0 and tmax=50
tmin = 0
tmax = 50
t = timeseries[:,0]
values = timeseries[:,1]
indices_within_time_interval = (t >= tmin) & (t <= tmax)
fig1, ax1 = plt.subplots()
ax1.plot(
    t[indices_within_time_interval], values[indices_within_time_interval]
)

# Compute and plot PDF estimate
hist, bin_edges = np.histogram(timeseries[:, 1], bins=100)
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[0:-1])

fig2, ax2 = plt.subplots()
ax2.plot(bin_centers, hist, "*")

# Now plot the "true" histogram (gaussian PDF)
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

hist, bin_edges = get_theoritical_histogram(
    np.amin(bin_edges), np.amax(bin_edges), std, mean
)
ax2.plot(bin_centers, hist)

plt.show()
