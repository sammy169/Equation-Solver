import quadratic

a = float(input("Enter your A value:"))
b = float(input("Enter your B value:"))
c = float(input("Enter your C value:"))

x1, x2 = quadratic.solver(a,b,c)

if x1 == x2:
    print(f'The solution is {x1}.')
else:
    print(f'First solution is {x1} and the second one is {x2}')
