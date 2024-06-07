# convert seconds to years
# completing exercises in a primer to scientific computing with python by Langtengen

# ask how many seconds we want to convert

s = float(input("Enter a how many seconds you want to convert: "))

y = s / 31536000

print(str(s) + 'seconds is equivalent to ' + str(y) + ' years')
