# WAP to Determine Whether a Given Number is Even or Odd Recursively

def check(n):
    if(n<2) :
        return n%2 == 0
    else:
        return check(n-2)

num = int(input("Please enter a number.."))

if(check(num) == True):
    print("Number is even!")
else:
    print("Number is odd!")