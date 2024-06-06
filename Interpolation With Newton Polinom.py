import numpy as np
import matplotlib.pyplot as plt

# Data Tegangan (x) dan Waktu patah (y)
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi Newton
def newton_interpolation(x_points, y_points, x):
    n = len(x_points)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y_points

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x_points[i + j] - x_points[i])

    def newton_basis(j, x):
        terms = [(x - x_points[i]) for i in range(j)]
        return np.prod(terms, axis=0)
    
    return sum(divided_diff[0, j] * newton_basis(j, x) for j in range(n))

# Range untuk x dari 5 sampai 40
x_range = np.linspace(5, 40, 500)

# Menghitung hasil interpolasi
y_newton = newton_interpolation(x, y, x_range)

# Plot hasil interpolasi
plt.figure(figsize=(14, 8))
plt.plot(x_range, y_newton, label='Hasil Interpolasi', color='green')
plt.scatter(x, y, color='red', label='Titik Data')
plt.title('Interpolasi Polinom dengan Metode Newton')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.grid(True)
plt.show()