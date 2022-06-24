# WAP to Find Prime Numbers in a Given Range

upper = int(input("Enter the upper limit"))

for i in range(2, upper + 1):
    count = 0

    for j in range(2, i//2+1):
        if i%j == 0:
            count = count + 1
    
    if(count <= 0):
        print(i)

