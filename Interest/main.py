# exercise 1.6 from Langtangen
p = float(input("Enter the initial balance: "))
B = float(input("What is the interest rate: "))
n = float(input("How long will the money be in the account (in years): "))

A = p*(1 + B/100)**n

print("The balance after", n,  "years is", "%.2f" % A)
