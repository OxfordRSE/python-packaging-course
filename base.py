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
hist, bin_edges = np.histogram(x[:,1], bins=100, density=True)
bin_centers = 0.5*(bin_edges[1:]+bin_edges[0:-1])
plt.figure(2)
plt.plot(bin_centers, hist, "*")
# Plot gaussian distribution
std_inverse = 1./std
normalisation = std_inverse/np.sqrt(2.0*np.pi)
gaussian = lambda x : normalisation*np.exp(-(x-mean)*(x-mean)*0.5*std_inverse)
fluctuation_domain = np.linspace(min(bin_centers),max(bin_centers),100)
plt.plot(fluctuation_domain, gaussian(fluctuation_domain))
plt.show()


