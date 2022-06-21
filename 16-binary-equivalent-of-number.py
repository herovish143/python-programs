# WAP to Print Binary Equivalent of a Number without Using Recursion

num = int(input("Please enter a number \n"))

lst = []

while num > 0 :
    dig = num % 2
    lst.append(dig)
    num = num // 2

lst.reverse()
print("Binary Equivalent number")

for i in lst:
    print(i, end = " ")