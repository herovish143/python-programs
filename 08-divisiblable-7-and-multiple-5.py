# Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers

lower = int(input("Please enter the lower limit (number) \n"))
upper = int(input("Please enter the upper limit (number) \n"))

for i in range(lower, upper+1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)