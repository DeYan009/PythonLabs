import numpy as np
from scipy.stats import multivariate_normal
import time


def log_multivariate_normal_pdf(X, m, C):
    D = X.shape[1]
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    diff = X - m
    exponent = -0.5 * np.sum(diff @ inv_C * diff, axis=1)
    log_pdf = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C) + exponent
    return log_pdf


# Тест
N, D = 100000, 10
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = C @ C.T

# Время lmn
start = time.time()
my_result = log_multivariate_normal_pdf(X, m, C)
my_time = time.time() - start

# Время scipy
start = time.time()
scipy_result = multivariate_normal(m, C).logpdf(X)
scipy_time = time.time() - start

# Сравнение точности
accuracy = np.max(np.abs(my_result - scipy_result))

print(f"Моя функция: {my_time:.9f} сек, Scipy: {scipy_time:.9f} сек, Точность: {accuracy}\n")
