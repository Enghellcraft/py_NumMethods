import numpy as np
from scipy.interpolate import lagrange

coefs = []

# Funs
def my_lagrange(x_values, y_values, x_new):
    #Where x_values are the values from dataset X
    # y_values are the values from dataset Y
    # x_new are the new values
    
    if len(x_values) != len(y_values):
        raise ValueError("x_values e y_values deben tener la misma")
    result = 0
    for i, x_i in enumerate(x_values):
        l_i = np.prod([(x_new - x_values[j])/(x_i - x_values[j]) for j in range(len(x_values)) if j != i])
        coefs.append(l_i)
        result += l_i * y_values[i]
    return result

# Dataset Parables
x = np.array([0, 1, 2])
y = np.array([1, 3, -2])

poly = lagrange(x, y)
print(np.poly1d(poly))

x_eval = [0, 1, 2]
for x_i in x_eval:
    print(f"Los valores por Lagrange son x = {x_i}: y = {my_lagrange(x, y, x_i)}")
    
# Dataset Linear
x = np.array([0, 1, 2])
y = np.array([1, 2, 3])

poly = lagrange(x, y)
print(np.poly1d(poly))

x_eval = [0, 1, 2]
for x_i in x_eval:
    print(f"Los valores por Lagrange son x = {x_i}: y = {my_lagrange(x, y, x_i)}")