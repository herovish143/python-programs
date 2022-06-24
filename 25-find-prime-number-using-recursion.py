# WAP  to Check whether a Number is Prime or Not using Recursion

def checkPrime(num, div = None):

    if (div == None):
        div = num - 1
    
    while div >= 2:
        if num % div == 0:
            print("Number is not prime", num)
            return False
        else:
            return checkPrime(num, div - 1)
    else:
        print("Number is prime ", num)
        return True

num = int(input("Enter a number to check prime"))

checkPrime(num)

