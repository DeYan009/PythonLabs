import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Настройки графика
plt.figure(figsize=(10, 6))
x = np.linspace(-1, 1, 400)

# Построение полиномов Лежандра от 1 до 7 степени
for n in range(1, 8):
    Pn = legendre(n)
    y = Pn(x)
    plt.plot(x, y, label=f'n = {n}')

# Оформление графика
plt.title('Полиномы Лежандра')
plt.grid(True)
plt.legend()
plt.show()