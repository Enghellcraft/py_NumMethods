#newton:
#  X = X0 - F(x)
#          _______
#           F'(x)

#Se define una funcion real cuya raiz sea la funcion dada:
# G(ln(x)) = 0

#La funcion puede obtenerse mediante Taylor, en este caso de orden 2:
# F(x) = ln(x)
# F'(x) = 1 / x
# F''(x) = -1 / X^2

# g(x) = f(x) + f'(x) . (x - x0) + [f''(x) / 2!] . (x - x0)^2 
# g(x) = - 1/2 x^2 + 2x - 3/2

# esto es para un punto solo
# generico deberia ser g(X) = e^x - a

from inspect import *
from sympy import *
import sympy as sp

x = symbols('x')

def f(x):
    # a very complicated function
    y = ln(x)
    return y

def get_polynomial(function, x0, degree):
    # parse function definition code

    lines_list  = getsource(function).split("\n")
    for line in lines_list:
        if '=' in line:
            func_def = line

    elements = func_def.split('=')
    line = ' '.join(elements[1:])
    sympy_function = sp.sympify(line)

    # compute taylor expansion symbolically 
    i = 0
    taylor_exp = sp.Integer(0)
    while i <= degree:
        taylor_exp = taylor_exp + (sp.diff(sympy_function,x,i).subs(x,x0))/(sp.factorial(i))*(x-x0)**i
        i += 1

    return taylor_exp

polynomialT = get_polynomial(f,1,2)

print ("Polynomial function whith ln(x) as root is:", polynomialT)

def my_newton(f, x0, e):
    # output is an estimation of the root of f 
    # using the Newton method
    # recursive implementation
    df=diff(f,x,1)
    
    if Abs((f.subs(x,x0)).evalf()) < e+0*I:
        return x0
    else:
       return my_newton(f, x0 - ((f/df).subs(x,x0).evalf()), e)
   
r = my_newton(polynomialT, 1, 0.1)

print("root =", r)