# Amusement Park Rides

Age_first_person = int(input("What is the age of the first rider?: "))
height_first_person = float(input("What is the height of the first rider? in inches: "))
second_rider = input("Is there a second rider (yes/no)?: ").lower()
print()

# One Person
if second_rider == "no":
    if Age_first_person >= 18 and height_first_person >= 62:
        print("You can ride alone")
    elif height_first_person < 36:
        print("You can't ride")
    elif Age_first_person < 18 or height_first_person < 62:
        print("You can't ride")
        print()
# Second Person
elif second_rider == "yes":
    Age_second_person = int(input("What is the age of the second rider?: "))
    height_second_person = float(input("What is the height of the second rider? in inches: "))

    if height_first_person < 36 or height_second_person < 36:
        print("One of you don't have the minimal height")
    elif height_first_person >= 36 and height_second_person >= 36 and Age_first_person >= 18 or Age_second_person >= 18:
        print("Welcome to the ride. Please be safe and have fun!")
    elif height_first_person >= 36 and height_second_person >= 36 and Age_first_person < 18 and Age_second_person < 18:
        print("Sorry, you may not ride.")
