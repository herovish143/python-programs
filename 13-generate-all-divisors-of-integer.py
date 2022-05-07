# Python Program to Generate all the Divisors of an Integer
num = int(input("Please enter a number"))

print("The divisors of the number are:")

for i in range(1, num+1):
    if num % i == 0:
        print(i)