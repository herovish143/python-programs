# Python Program to Print Odd Numbers Within a Given Range

upper = int(input("Please enter the upper limit"))
lower = int(input("Please enter the lower limit"))

for i in range(lower, upper+1):
    if(i%2 !=0):
        print(i)