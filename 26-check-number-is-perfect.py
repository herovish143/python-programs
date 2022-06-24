# to Check Whether a Given Number is Perfect Number

num = int(input("Enter a number"))

sum1 = 0

for i in range(1, num):
    if num % i == 0:
        sum1 = sum1 + i

if sum1 == num:
    print("Number is perfect", num)
else:
    print("Number isn't perfect", num)
