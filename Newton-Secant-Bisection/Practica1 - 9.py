import numpy as np
import sympy as sp
from sympy import *

#Derivative fun
x = symbols('x')

#Newton fun
def my_newton(f, x0, e):
    # output is an estimation of the root of f 
    # using the Newton method
    # recursive implementation
    df=diff(f,x,1)
    
    print(x0)
    
    if Abs((f.subs(x,x0)).evalf()) < e+0*I:
        return x0
    else:
       return my_newton(f, x0 - ((f/df).subs(x,x0).evalf()), e)

#a)
f1 = x**2-2*x+1 
r1 = my_newton(f1, -2, 0.001)
print("root 1 =", r1)