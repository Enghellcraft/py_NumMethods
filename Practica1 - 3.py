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

f1 = x**(0.5)
#r1 = my_newton(f1, 1, 0.1) cannot be solved by this method due to root result repetitions in iterations

f2 = x**3+1
r2 = my_newton(f2, 2, 0.1)

f3 = x**3 - x + 1
r3 = my_newton(f3, 0, 0.1)

f4 = (exp(-x)) - sin(x)
r4 = my_newton(f4, 3, 0.1)

f5 = 2/x
r5 = my_newton(f5, 1, 0.1)

f6 = Abs(x + 5)
#r6 = my_newton(f6, 10, 0.1)

f7 = 2*x + 3
r7 = my_newton(f7, 2, 0.1)

#Results
#print("f(r1) =", f1(r1))
print("root 2 =", r2)
print("root 3 =", r3)
print("root 4 =", r4)
print("root 5 = has none, has limits to zero")
print("root 6 = cannot be found due to positive values for absolutes")
print("root 7 =", r7)

