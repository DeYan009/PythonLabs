import numpy as np


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
zero_indices = np.where(x[:-1] == 0)[0]
elements_after_zero = x[zero_indices + 1]

if len(elements_after_zero) > 0:
    max_element = np.max(elements_after_zero)
else:
    max_element = None

print(f"Максимальный элемент после нуля: {max_element}")
