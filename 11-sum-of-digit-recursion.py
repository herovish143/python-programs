# Python Program to Compute the Sum of Digits in a given Integer

num = int(input("Please enter any number for sum \n"))

total = 0

while(num > 0):
    dig = num % 10;
    
    total = total + dig
    
    num = num//10

print(total)