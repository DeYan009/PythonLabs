import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Настройка фигуры
fig, ax = plt.subplots(figsize=(8, 8))
line, = ax.plot([], [])
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
ax.set_title('Фигуры Лисажу с изменяющимся соотношением частот')

# Функция инициализации
def init():
    line.set_data([], [])
    return line,

# Функция обновления кадра
def update(frame):
    a = frame
    b = 1
    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(a * t)
    y = np.sin(b * t)
    line.set_data(x, y)
    ax.set_title(f'Соотношение частот {a:.2f}:{b}')
    return line,

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100),
                    init_func=init, blit=True, interval=50)
plt.show()