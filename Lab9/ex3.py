import numpy as np


array = np.random.normal(size=(10, 4))

min_val = np.min(array)
max_val = np.max(array)
mean_val = np.mean(array)
std_val = np.std(array)

first5 = array[:5].copy()

print(f"Минимум: {min_val}, Максимум: {max_val}, Среднее: {mean_val}, Стандартное отклонение: {std_val}")
print("Первые 5 строк:")
print(first5, "\n")
