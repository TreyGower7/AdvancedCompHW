import numpy as np
import matplotlib.pyplot as plt

# Function f(x) = sin(πx)
def f(x):
    return np.sin(np.pi * x)

# Mesh generation
mesh_points = np.linspace(0, 1, 5)  # Generate five points from 0 to 1
# Calculate function values at mesh points
f_values = f(mesh_points[0:5]) 
y = np.zeros(np.shape(f_values))
# Plotting the function f(x) = sin(πx)
x_values = np.linspace(0, 1, 1000)  
plt.figure(figsize=(8, 6))
plt.plot(x_values, f(x_values), label='f(x) = sin(πx)', color='blue')

# Piecewise linear interpolant fh
plt.scatter(mesh_points[0:5], f_values, color='red', label='fh(xi) = sin(πxi)', zorder=5)

# Connect the points to visualize 
for i in range(4):
    plt.plot(mesh_points[0:i+2], f_values[0:i+2], color='red', linestyle='--')

#Plot
plt.title('Finite Element Interpolant')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.savefig('FE_Interpolant.jpg')
