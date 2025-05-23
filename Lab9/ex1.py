import numpy as np


matrix = np.loadtxt('matrix.txt', delimiter=',')

total_sum = np.sum(matrix)
max_element = np.max(matrix)
min_element = np.min(matrix)

print(f'Сумма: {total_sum}, Максимальный: {max_element}, Минимальный: {min_element}')
