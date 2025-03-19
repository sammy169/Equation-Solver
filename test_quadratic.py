import quadratic


# test case for imaginary numbers
a = 1
b = 5
c = 7

x1, x2 = quadratic.solver(a,b,c)
print (f"first : {x1}, {x2}")


# test case for a single solution 
a = 1
b = 2
c = 1

x1, x2 = quadratic.solver(a,b,c)
assert(x1==x2)
print (f"second : {x1}, {x2}")


# test case for a regular quadratic equation 
a = 1
b = 5
c = 3

x1, x2 = quadratic.solver(a,b,c)
print (f"third : {x1}, {x2}")
