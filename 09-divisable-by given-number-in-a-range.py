#Python Program to Print all Numbers in a Range Divisible by a Given Number

lower = int(input("Please enter the lower limit (number) \n"))
upper = int(input("Please enter the upper limit (number) \n"))

given_num = int(input("enter the number two check \n"))

for i in range(lower, upper+1):
    if(i % given_num == 0):
        print(i)