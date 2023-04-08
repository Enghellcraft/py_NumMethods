import numpy as np
import sympy as sp
from sympy import *

#Convergence Fun

def convergence(n):
    number = n
    for i in range(10):
        number = (number / 2) + (1 / number)
        print(number)
    return number

conv = convergence(1)

print ("Convergence after 10 iterations: ", conv)