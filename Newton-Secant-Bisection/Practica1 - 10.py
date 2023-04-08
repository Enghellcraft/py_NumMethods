# if the derivative at a guess is close to 0, then the Newton step will be very large and 
# probably lead far away from the root. Also, depending on the behavior of the function derivative 
# between x0 and xr, the Newton-Raphson method may converge to a different root than xr that may not be useful 

# Compute a single Newton step to get an improved approximation of the root of the function f(x)=x^3+3x^2−2x−5 and an initial guess, x0=0.29.
# Note that f′(x0)=−0.0077 (close to 0) and the error at x1 is approximately 324880000 (very large).
# x1 = -688.4516883116648

# We could add a little epsilon to the Xn, in order to prevent going so far,
# but we risk getting it much worse than before