# WAP to Check Armstrong Number

num = int(input("Enter any number"))

# way1
sum1 = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum1 += digit ** 3
    temp //= 10

if num == sum1 :
    print("Number is Armstrong", num)
else:
    print("Number is not a Armstrong", num)


# way 2
lst1 = list(map(int, str(num)))
lst2  = list(map(lambda x:x**3, lst1))

print(lst1, lst2)

if (sum(lst2) == num):
    print("Number is ArmStrong", num)
else:
    print("Number is not ArmStrong", num)
