import numpy as np
import sympy as sp
from sympy.abc import x

# Funs
def my_divided_diff(x, y):
    # takes X and Y from the dataset given
    n = len(y)
    
    # creates a matrix, the size of one variable data (datapoints),containing zeros
    coef = np.zeros([n, n])
    
    # sets Y values of dataset to the first column
    coef[:,0] = y
    
    # iterates through the second column 
    for j in range(1,n):
        for i in range(n-j):
            # calculates the jth divided difference coefficient
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
           
    # returns matrix of coefficients        
    return coef

def my_newton_poly(coef, x_data, x):
# where coef is a matrix of coefficients from my_divided_diff
# x_data is the array of x values of the dataset
# x is the array of new X values to witch the Newton poly will evaluate

    n = len(x_data) - 1 
    
    # initialized in the last coefficient of the matrix
    p = coef[n]
    #poly_str = str(p)
    
    # iterates reversely through the matrix
    for k in range(1,n+1):
        # for each coefficient, updates p
        p = coef[n-k] + (x -x_data[n-k])*p
        
        # returns polynomial
       # poly_str = f"{coef[n-k]:+}" + poly_str + f"({x-x_data[n-k]})"
    return p #poly_str

# Dataset
x = np.array([0, 1, 2, 3])
y = np.array([1, 1, 1, 2])

# get the divided difference coef first row
a_s = my_divided_diff(x, y)[0, :]

# new values stored
newton_poly_str = np.poly1d(a_s[::-1])

# a) 
print(newton_poly_str)

x_eval = [0, 1, 2, 3, -1, 2, 4]
for x_i in x_eval:
    y_i = my_newton_poly(a_s, x, x_i)
    print(f"Los valores por Newton son x = {x_i}: y = {y_i}")
    
