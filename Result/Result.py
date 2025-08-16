sub1 = int(input("Enter marks for Sub 1: "))
sub2 = int(input("Enter marks for Sub 2: "))
sub3 = int(input("Enter marks for Sub 3: "))
sub4 = int(input("Enter marks for Sub 4: "))
sub5 = int(input("Enter marks for Sub 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total / 5
per = (total / 500) * 100 

if per >= 90:
    grade = "A+"
elif per >= 80:
    grade = "A"
elif per >= 70:
    grade = "B"
elif per >= 60:
    grade = "C"
elif per >= 50:
    grade = "D"
else:
    grade = "F"

print("\nResult")
print("Total Marks:", total)
print("avg:", round(avg, 2))
print("Per:", round(per, 2), "%")
print("Grade:", grade)