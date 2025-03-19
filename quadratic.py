import math
import cmath
import sys

# Takes input a,b,c which are the coefficionts of quadriatic equations
#then uses the quadratic formula to compute the result and returns it to the user

def solver(a, b, c):
    p = b*b - 4*a*c
    if p < 0:
        x1 = ((b*-1) + cmath.sqrt(p))/(2*a)
        x2 = ((b*-1) - cmath.sqrt(p))/(2*a)
    else:
        x1 = ((b*-1) + math.sqrt(p))/(2*a)
        x2 = ((b*-1) - math.sqrt(p))/(2*a)

    return x1, x2
