import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the constants and the number of basis functions
k = 1.0  # Assuming a constant for simplicity
N = 3  # Number of basis functions

# Define the basis functions and their derivatives
def basis_function(x, i):
    return np.sin(i * np.pi * x)

def basis_derivative(x, i):
    return i * np.pi * np.cos(i * np.pi * x)

# Define the function f(x)
def f_x(x):
    return x  

def exact_solution(x):
    return -(1/6) * x**3 + (1/2) * x**2

# Stiffness matrix calculation
K = np.zeros((N, N))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        integrand = lambda x: k * basis_derivative(x, i) * basis_derivative(x, j)
        K[i - 1, j - 1], _ = quad(integrand, 0, 1)  # Assuming limits 0 to 1

print("Stiffness Matrix (K):\n", K)

# Load vector calculation

f = np.zeros(N)

for i in range(1, N + 1):
    integrand = lambda x: f_x(x) * basis_function(x, i)
    f[i - 1], _ = quad(integrand, 0, 1)  # Assuming limits 0 to 1

print("Load Vector (f):\n", f)

coeff = np.linalg.solve(np.linalg.inv(K),f)

print(coeff)

x_values = np.linspace(0, 1,100)  # Generating x values for plotting
y_h = np.zeros_like(x_values)

for i in range(N):
    y_h += coeff[i] * basis_function(x_values, i + 1)

# Calculate y values for the exact solution
y_exact = exact_solution(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_h, label='Approximate Solution (y_h)')
# Plot the exact solution
plt.plot(x_values, y_exact, label='Exact Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exact vs Approximate Solution to -y\'\' = x')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('approximate_vs_exact.jpg')




