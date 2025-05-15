import numpy as np
import matplotlib.pyplot as plt

# Генерация нормального распределения
mu, sigma = 0, 1  # среднее и стандартное отклонение
s = np.random.normal(mu, sigma, 10000)

# Отрисовка гистограммы
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp(-(bins - mu)**2 / (2 * sigma**2)),
         linewidth=2, color='r')
plt.title('Нормальное распределение')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.grid(True)
plt.show()