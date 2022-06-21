# WAP to Reverse a Given Number

from os import remove


num = int(input("Enter a number to reverse ... "))
rev = 0
while(num>0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num//10

print(rev)