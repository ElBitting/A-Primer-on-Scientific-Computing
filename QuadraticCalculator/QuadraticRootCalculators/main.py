from numpy.lib.scimath import *

a = float(input("Enter the leading coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the constant term: "))

r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print("The roots of the polynomial are "+str(r1) + " and " + str(r2))
