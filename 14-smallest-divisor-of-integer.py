# Python Program to Find the Smallest Divisor of an Integer

num = int(input('Please enter a number'))
divisors=[]

for i in range(2, num+1):
    if num%i == 0:
        divisors.append(i)

divisors.sort()

print("Smallest divisor is: ", divisors[0])