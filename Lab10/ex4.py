import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Настройка фигуры и осей
fig = plt.figure(figsize=(12, 8))
plt.subplots_adjust(bottom=0.4)

# Создание осей для графиков
ax1 = plt.subplot2grid((3, 2), (0, 0))  # Волна 1
ax2 = plt.subplot2grid((3, 2), (0, 1))  # Волна 2
ax3 = plt.subplot2grid((3, 2), (1, 0), colspan=2, rowspan=2)  # Сумма волн

# Исходные данные
x = np.linspace(0, 4 * np.pi, 1000)
line1, = ax1.plot(x, np.sin(x))
line2, = ax2.plot(x, np.sin(x))
line_sum, = ax3.plot(x, np.sin(x) + np.sin(x))

# Настройка графиков
for ax, title in zip([ax1, ax2, ax3], ['Волна 1', 'Волна 2', 'Сумма волн']):
    ax.grid(True)
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(-2, 2)
    ax.set_title(title)

# Создание слайдеров
ax_amp1 = plt.axes([0.15, 0.25, 0.3, 0.03])
ax_freq1 = plt.axes([0.15, 0.2, 0.3, 0.03])
ax_amp2 = plt.axes([0.55, 0.25, 0.3, 0.03])
ax_freq2 = plt.axes([0.55, 0.2, 0.3, 0.03])

slider_amp1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=1)
slider_freq1 = Slider(ax_freq1, 'Частота 1', 0.5, 5.0, valinit=1)
slider_amp2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=1)
slider_freq2 = Slider(ax_freq2, 'Частота 2', 0.5, 5.0, valinit=1)


# Функция обновления
def update(val):
    amp1 = slider_amp1.val
    freq1 = slider_freq1.val
    amp2 = slider_amp2.val
    freq2 = slider_freq2.val

    y1 = amp1 * np.sin(freq1 * x)
    y2 = amp2 * np.sin(freq2 * x)

    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line_sum.set_ydata(y1 + y2)

    for ax in [ax1, ax2, ax3]:
        ax.set_ylim(-(amp1 + amp2 + 0.1), amp1 + amp2 + 0.1)

    fig.canvas.draw_idle()


# Привязка событий
slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

plt.show()