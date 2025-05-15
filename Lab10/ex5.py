import numpy as np
import matplotlib.pyplot as plt

# Создание фигуры с двумя 3D графиками
fig = plt.figure(figsize=(14, 6))

# Подготовка данных
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # Функция MSE

# Первый график (обычный масштаб)
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('MSE в обычном масштабе')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')

# Второй график (логарифмический масштаб по Z)
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, np.log10(Z + 1e-10), cmap='plasma')
ax2.set_title('MSE в логарифмическом масштабе (Z)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log10(MSE)')

plt.tight_layout()
plt.show()