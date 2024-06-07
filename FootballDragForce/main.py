from numpy import *

r = float(input("Enter the radius of the ball (in meters): "))
m = float(input("Enter the mass of the ball (in kilograms): "))
g = 9.81
C = 0.4
A = pi * r**2
V = float(input("Enter the velocity of the ball (in m/s): "))
D = 1.2

if r < 0:
    r = float(input("Error, please enter a positive radius: "))
if m < 0:
    m = float(input("Error, please enter a positive mass: "))

DragForce = 1/2 * C * D * A * V**2
GravForce = m * g
ratio = DragForce / GravForce

print("The drag force on the ball is", "%.1f" % DragForce)
print("The gravitational force on the ball is", "%.1f" % GravForce)
print("The ratio between DragForce and GravForce is", str(ratio) + ":1")
