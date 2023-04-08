import numpy as np
import math as math

#Bisecction Fun
def my_bisection(f, a, b, e): 
    # approximates a root, R, of f bounded 
    # by a and b to within eerance 
    # | f(m) | < e with m the midpoint 
    # between a and b Recursive implementation
    print(f(a), f(b))
    
    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        return("There is no root between a and b")
        
    # get midpoint
    m = (a + b)/2
    
    if np.abs(f(m)) <= e:
        # stopping condition, report m as root
        return m
    
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return my_bisection(f, m, b, e)
    
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return my_bisection(f, a, m, e)
    

#Data    
euler = math.e

print(euler)

f1 = lambda x: x**(1/2)
r1 = my_bisection(f1, 0, 2, 0.1)
print("root 1 =", r1)

f2 = lambda x: x**3 + 1
r2 = my_bisection(f2, -2, 0, 0.1)
print("root 2 =", r2)

f3 = lambda x: x**3 - x + 1
r3 = my_bisection(f3, -2, 0, 0.1)
print("root 3 =", r3)

f4 = lambda x: (euler**(-x)) - math.sin((x*math.pi)/180)
r4 = my_bisection(f4, 2.8, 3, 0.1)
print("root 4 =", r4)

f5 = lambda x: 2/x
r5 = my_bisection(f5, 100, 10000, 0.1)
print("root 5 =", r5)

f6 = lambda x: abs(x + 5)
r6 = my_bisection(f6, -10, 10, 0.1)
print("root 6 =", r6)

f71 = lambda x: 2*x + 3
r71 = my_bisection(f71, -4, 2, 0.1)
print("root 71 =", r71)

f72 = lambda x: 2*x + 3
r72 = my_bisection(f72, -4, 2, 0.001) #first two decimals should be true
print("root 72 =", r72)

#Results
print("f(r1) =", f1(r1))
print("f(r2) =", f2(r2))
print("f(r3) =", f3(r3))
print("f(r4) =", f4(r4))
print("f(r5) = has none, has limits to zero")
print("f(r6) = cannot be found due to positive values for absolutes")
print("f(r71) =", f71(r71))
print("f(r72) =", f72(r72))