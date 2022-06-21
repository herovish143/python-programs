# WAP to Count the Number of Digits in a Number
num = int(input("Please enter a number to get count of digits"))

count = 0

while(num > 0):
    count = count + 1
    num = num // 10

print("The number of digits in the number are: ", count)
