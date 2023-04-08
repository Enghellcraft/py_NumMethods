import numpy as np
import sympy as sp
from sympy import *

x = symbols('x')

# a to b interval values
def abInterval(f,n):
    if ((f.subs(x,n)).evalf() < 0):
        next = n
        i = 0
        while (f.subs(x,next)).evalf() < 0:
            i = i + 1
            next = next + 1
            if (i == 10):
                print("Not b found")
                break
        while (f.subs(x,next)).evalf() < 0:
            next = next + 2
            if (i == 20):
                print("Not b found")
                break
        if ((f.subs(x,next)).evalf() > 0):
            print("The second interval value is b= ",next)
        return ("The first interval value is a= ",n) 
    else:
        next = n
        i = 0
        while (f.subs(x,next)).evalf() > 0:
            i = i + 1
            next = next + 1
            if (i == 10):
                print("Not b found")
                break
        while (f.subs(x,next)).evalf() > 0:
            next = next + 2
            if (i == 20):
                print("Not b found")
                break
        if ((f.subs(x,next)).evalf() > 0):
            print("The second interval value is b= ",next)
        return ("The first interval value is a= ",n) 
    
#Data
f1 = x + 2

abInterval(f1, 2)   
