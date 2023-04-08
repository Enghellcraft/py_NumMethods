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
    print(m)
    
    if np.abs((f.subs(x,m)).evalf()) <= e:
        # stopping condition, report m as root
        return m
    
    elif np.sign((f.subs(x,a)).evalf()) == np.sign((f.subs(x,m)).evalf()):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return my_bisection(f, m, b, e)
    
    elif np.sign((f.subs(x,b)).evalf()) == np.sign((f.subs(x,m)).evalf()):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return my_bisection(f, a, m, e)
  
# Secant Fun
def my_secant(f,x0,x1,e,N):
    step = 1
    condition = True
    while condition:
        if (f.subs(x,x0)).evalf() == (f.subs(x,x1)).evalf():
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*(f.subs(x,x0)).evalf()/( (f.subs(x,x1)).evalf() - (f.subs(x,x0)).evalf() ) 
        print('Iteration %d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, (f.subs(x,x2)).evalf()))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs((f.subs(x,x2)).evalf()) > e
    return(x2)
    
        
#Data

f1 = x + 2

#a)
newtonRoot = my_newton(f1, 2, 0.001)
print("Newton Root: ", newtonRoot)

#b)
bisectionRoot = my_bisection(f1, -2, 0, 0.001)
print("bisection Root: ", bisectionRoot)

#c)
secantRoot = my_secant(f1, -2, 0, 0.001, 15)
print("secant Root: ", secantRoot)