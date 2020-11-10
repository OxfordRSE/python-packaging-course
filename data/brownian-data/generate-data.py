import numpy as np
import csv

dt = 0.1
T = 1000

mu = 0.0
D = 1.0
x = 0.0

with open('./data/brownian.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    for t in np.arange(0, T, dt):
        dw = np.random.normal(0.0, np.sqrt(dt))
        x = x + (mu-x)*dt + np.sqrt(2.0*D)*dw
        csvwriter.writerow([t, x])
