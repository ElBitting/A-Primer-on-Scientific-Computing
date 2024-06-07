from numpy import *

x = float(input("Enter a number: "))
m = float(input("Enter a number greater than 0: "))
s = float(input("Enter a number greater than 0: "))

if s <= 0:
    s = float(input("Error, please enter a positive number: "))
if m < 0:
    m = float(input("Error, please enter a number greater than 0: "))

final = (1/sqrt( 2 * pi)) * exp((-0.5) * (( x - m )/s)**2)

print(final)