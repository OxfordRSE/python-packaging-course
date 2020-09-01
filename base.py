import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("./data/brownian.csv", delimiter=",")
dt = 0.1

# Plot trajectory between t=0 and t=50
T = 50
n = int(T/dt)+1
plt.figure(1)
plt.plot(x[0:n,0],x[0:n,1])

# Compute and print mean and standard deviation
mean = np.mean(x[:,1])
std = np.std(x[:,1])
print(f"The mean is {mean}")
print(f"The standard deviation is {std}")

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


