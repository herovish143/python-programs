# Python Program to Check if a Number is a Palindrome

num = int(input("Please enter the number to check is palidrome or not"))

tem_num = num

rev = 0

while(num>0):
    dig=num%10
    rev=rev*10+dig
    num = num//10

if(tem_num == rev):
    print("number is Palindrome")
else:
    print("number is not Palindrome")