# exercise 1.4 from Langtangen

m = float(input("Enter the amount of meters: "))

cm = m * 100
inches = cm / 2.54
feet = inches / 12
yard = feet / 3
miles = yard / 1760

print(str(m) + ' meters equals ' + str(inches) + ' inches, \n'
      + str(feet) + ' feet, ' + str(yard) + ' yards, \n'
      + 'and ' + str(miles) + ' miles.')
