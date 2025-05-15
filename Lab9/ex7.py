import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
species = iris[:, -1]
unique_values, counts = np.unique(species, return_counts=True)
for speciess, count in zip(unique_values, counts):
    print(f"{speciess.decode('utf-8')}: {count}")
