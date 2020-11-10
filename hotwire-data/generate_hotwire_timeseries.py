from datetime import date
import csv
from os import linesep
import sys
import h5py

with h5py.File('datajet.h5') as datafile:
    time = datafile['time'][:]
    data = datafile['velocity'][:]
    freq = datafile.attrs['sampl_freq']
    nu_air = datafile.attrs['viscosity']

with open('./data/hotwire.csv', 'w', newline='') as csvfile:
    headerstring = (f"# Generated with {sys.argv[0]} on {date.today()}{linesep}"
                    "# Subset of measurements of the longitudinal velocity "
                    "of a turbulent jet made in a wind tunnel at ENS de Lyon, "
                    f"by Christophe Baudet and Antoine Naert.{linesep}"
                    f"# Measurement frequency is {freq}Hz.{linesep}"
                    f"#{linesep}")

    csvfile.write(headerstring)
    csvwriter = csv.writer(csvfile, delimiter=",", lineterminator=linesep)
    for step, t in enumerate(time[:10000]):
        csvwriter.writerow([t, data[0, step]])
