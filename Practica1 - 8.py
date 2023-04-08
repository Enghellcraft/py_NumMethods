import math as math
import numpy as np
import sympy as sp
from sympy import *

#Bisecction Fun
def my_bisection(f, a, b, e): 
    # approximates a root, R, of f bounded 
    # by a and b to within eerance 
    # | f(m) | < e with m the midpoint 
    # between a and b Recursive implementation
    #print((f.subs(x,a)).evalf(), (f.subs(x,b)).evalf())
    
    # check if a and b bound a root
    if np.sign((f.subs(x,a)).evalf()) == np.sign((f.subs(x,b)).evalf()):
        return("There is no root between a and b")
        
    # get midpoint
    m = (a + b)/2
    
    if np.abs((f.subs(x,m)).evalf()) <= e:
        # stopping condition, report m as root
        return m
    
    elif np.sign((f.subs(x,a)).evalf()) == np.sign((f.subs(x,m)).evalf()):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        print("Right")
        return my_bisection(f, m, b, e)
        
    
    elif np.sign((f.subs(x,b)).evalf()) == np.sign((f.subs(x,m)).evalf()):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        print("Left")
        return my_bisection(f, a, m, e)
    
#Data
x = symbols('x')

f2 = -2*x + 2

#Results
#a)
r2 = my_bisection(f2, -5, 0, 0.001)
print("root 2 =", r2)
r2 = my_bisection(f2, -10, 1, 0.001)
print("root 2 =", r2)

#b) False, in the precious example root convergence is nearer to the last point of the interval
