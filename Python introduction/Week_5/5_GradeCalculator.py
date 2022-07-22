# Grade Calculator

grade_percentage = int(input("Enter your grade percentage:"))
print()

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80 and grade_percentage < 90:
    letter = "B"
elif grade_percentage >= 70 and grade_percentage < 80:
    letter = "C"
elif grade_percentage >= 60 and grade_percentage < 70:
    letter = "D"
else:
    letter = "F"

print(f"Your grade is: {letter}")

print()
if grade_percentage >= 70:
    print("Congratulation! you passed the course")
else:
    print("Sorry! you did not passed the course. Try harder the next time!\n")
