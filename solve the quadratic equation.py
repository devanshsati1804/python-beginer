import cmath

a =int(input("enter the value A"))
b =int(input("enter the value B"))
c =int(input("enter the value C"))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))