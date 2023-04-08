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
    
    if Abs((f.subs(x,x0)).evalf()) < e+0*I:
        return x0
    else:
       return my_newton(f, x0 - ((f/df).subs(x,x0).evalf()), e)

#Data
#a)
f1 = 3/x
#r1 = my_newton(f1, 0, 0.01)
print("Can't find root of function due to Asintote as initial value X = 0")
r1 = my_newton(f1, 15, 0.01)
print("Funtion:f1 = 3/x, with initial value 15: ", r1)

#b)
f2 = x + 2
r2 = my_newton(f2, -10, 0.01)
print("Funtion:f2 = x + 2, with initial value -10: ", r2)
r2 = my_newton(f2, 0, 0.01)
print("Funtion:f2 = x + 2, with initial value 0: ", r2)
r2 = my_newton(f2, 10, 0.01)
print("Funtion:f2 = x + 2, with initial value 10: ", r2)

#c) 
f3 = x**(0.5)
#r3 = my_newton(f3, 1, 0.01) cannot be solved by this method due to root result repetitions in iterations between 0.1 and -0.1
print("Can't find root of function due to repetitions in iterations between 0.1 and -0.1")

#d) New loses cuadratic convergence when the function has multiplicity in roots
f4 = x**2 - 2*x + 1
r4 = my_newton(f4, 10, 0.01)
print("Funtion:f4 = x**2 - 2*x + 1, with initial value 10: ", r4)
