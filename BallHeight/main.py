# ball throwing height calculator

g = 9.81  # gravity
v0 = float(input("What is the initial velocity (in m/s): "))  # input should be m/s
t = float(input("What time do you want to check: "))  # time is in seconds


while t < 0:  # if input doesn't make sense, redo
    print('Error, the time must be greater than zero.')
    t = float(input("What is the time you want to check: "))


y = v0 * t - g * t**2 / 2  # calculate location

if t > 2*v0/g or y == 0:  # hasn't left at t=0 and lands at >
    print("The ball is on the ground")
else:  # normal location
    print('The ball is', y, 'meters above the ground')
