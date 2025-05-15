import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Генерация прямоугольного сигнала
t = np.linspace(0, 1, 500, endpoint=False)
square_wave = signal.square(2 * np.pi * 5 * t, duty=0.5)

# Отрисовка сигнала
plt.figure(figsize=(10, 4))
plt.plot(t, square_wave)
plt.title('Прямоугольный сигнал')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.show()