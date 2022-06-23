# WAP to Read a Number n and Compute n+nn+nnn

num = int(input("Please enter a number "))

tem = str(num)

t1 = tem + tem

t2 = tem + tem + tem

comp = num + int(t1) + int(t2)

print("the value is", comp)
