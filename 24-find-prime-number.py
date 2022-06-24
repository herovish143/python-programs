# WAP to Check Prime Number

num = int(input("Enter the number to check prime number"))

count = 0

for i in range(2, num//2):
    if num%i == 0:
        count = count + 1

if count <= 0:
    print("Entered number is prime number", num)
else:
    print("Entered number is not a prime number", num)