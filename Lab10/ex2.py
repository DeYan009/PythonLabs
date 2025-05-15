import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку для 4 графиков
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]  # Соотношения частот
t = np.linspace(0, 2 * np.pi, 1000)  # Временная ось

# Построение каждой фигуры Лисажу
for i, (a, b) in enumerate(ratios):
    row = i // 2
    col = i % 2
    ax = axs[row, col]
    ax.plot(np.sin(a * t), np.sin(b * t))
    ax.set_title(f'Соотношение частот {a}:{b}')
    ax.grid(True)

plt.tight_layout()
plt.show()