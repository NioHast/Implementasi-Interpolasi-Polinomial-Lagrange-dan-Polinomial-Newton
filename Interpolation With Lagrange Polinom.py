import numpy as np
import matplotlib.pyplot as plt

# Data Tegangan (x) dan Waktu patah (y)

x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi Lagrange
def lagrange_interpolation(x_points, y_points, x):
    def L(k, x):
        terms = [(x - x_points[i]) / (x_points[k] - x_points[i]) for i in range(len(x_points)) if i != k]
        return np.prod(terms, axis=0)
    
    return sum(y_points[k] * L(k, x) for k in range(len(x_points)))

# Range untuk x dari 5 sampai 40
x_range = np.linspace(5, 40, 1000)

# Menghitung hasil interpolasi
y_lagrange = lagrange_interpolation(x_points, y_points, x_range)

# Plot hasil interpolasi
plt.figure(figsize=(14, 8))
plt.plot(x_range, y_lagrange, label='Hasil Interpolasi', color='blue')
plt.scatter(x_points, y_points, color='red', label='Titik Data')
plt.title('Interpolasi Polinom dengan Metode Lagrange')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.grid(True)
plt.show()