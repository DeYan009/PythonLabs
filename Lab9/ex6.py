import numpy as np


arr = np.arange(16).reshape(4, 4)
arr[[0, 2]] = arr[[2, 0]]


swapped_array = arr
print("Массив после замены строк 1 и 3:")
print(swapped_array, "\n")
