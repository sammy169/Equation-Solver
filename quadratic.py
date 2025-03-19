import math
import sys

a = float(input("Enter your A value:"))
b = float(input("Enter your B value:"))
c = float(input("Enter your C value:"))


# Takes input a,b,c which are the coefficionts of quadriatic equations
#then uses the quadratic formula to compute the result and returns it to the user

def solver(a, b, c):
    p = b*b - 4*a*c
    if p < 0:
        print('This number is not real')
        sys.exit(-1)
    
    x1 = ((b*-1) + math.sqrt(p))/(2*a)
    x2 = ((b*-1) - math.sqrt(p))/(2*a)

    return x1, x2


x1, x2 = solver(a,b,c)

print(f'First solution is {round(x1,3)} and the second one is {round(x2,3)}')