# WAP to Calculate Grade of a Student

sub1 = int(input("Please enter marks of subject 1 \n"))
sub2 = int(input("Please enter marks of subject 2 \n"))
sub3 = int(input("Please enter marks of subject 3 \n"))
sub4 = int(input("Please enter marks of subject 4 \n"))
sub5 = int(input("Please enter marks of subject 5 \n"))

average = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if average >= 90:
    print("Grade A")
elif (average >=80 and average < 90):
    print("Grade B")
elif (average >= 70 and average < 80):
    print("Grade C")
elif (average >=60 and average < 70):
    print("Grade D")
else:
    print("Grade F")