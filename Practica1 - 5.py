import numpy as np
import sympy as sp
from sympy import *

x = symbols('x')

f1 = x**2
df1=diff(f1,x,1)
print("Para la funcion:", f1, " la primer derivada es:", df1)

f2 = ln(x)
df2=diff(f2,x,1)
print("Para la funcion:", f2, " la primer derivada es:", df2)

f3 = sqrt(x)
df3=diff(f3,x,1)
print("Para la funcion:", f3, " la primer derivada es:", df3)

f4 = cos(x)
df4=diff(f4,x,1)
print("Para la funcion:", f4, " la primer derivada es:", df4)

f5 = 1/x
df5=diff(f5,x,1)
print("Para la funcion:", f5, " la primer derivada es:", df5)

f6 = sin(x/x)
df6=diff(f6,x,1)
print("Para la funcion:", f6, " la primer derivada es:", df6)
print ("F6 no cumple porque su primer derivada es cero")

def my_newton(f, x0, e):
    # output is an estimation of the root of f 
    # using the Newton method
    # recursive implementation
    df=diff(f,x,1)
    
    if Abs((f.subs(x,x0)).evalf()) < e+0*I:
        return x0
    else:
       return my_newton(f, x0 - ((f/df).subs(x,x0).evalf()), e)
   
r1 = my_newton(f1, 1, 0.1)
r2 = my_newton(f2, 2, 0.1)
r3 = my_newton(f3, 0, 0.1)
r4 = my_newton(f4, 3, 0.1)
r5 = my_newton(f5, 1, 0.1)
#r6 = my_newton(f6, 10, 0.1)

print("root 1 =", r1)
print("root 2 =", r2)
print("root 3 =", r3)
print("root 4 =", r4)
print("root 5 = ", r5)
#print("root 6 = ", r5)
