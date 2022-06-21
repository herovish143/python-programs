# WAP to Find the Binary Equivalent of a Number Recursively

lst = []

def convert(num):
    if(num == 0):
        return 1
    digit = num % 2
    lst.append(digit)
    convert(num//2)

nums = int(input("Please enter a number \n"))

convert(nums)

lst.reverse()

print("Binary equivalent:")
for i in lst:
    print(i,'\n')

