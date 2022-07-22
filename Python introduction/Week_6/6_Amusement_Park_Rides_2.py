# Amusement Park Rides

Age_first_person = int(input("What is the age of the first rider?: "))
height_first_person = float(input("What is the height of the first rider? in inches: "))
second_rider = input("Is there a second rider (yes/no)?: ").lower()

if second_rider == "yes":
    Age_second_person = int(input("What is the age of the second rider?: "))
    height_second_person = float(input("What is the height of the second rider? in inches: "))

    if Age_first_person >= 12 and Age_first_person < 18 or Age_second_person >= 12 and Age_second_person < 18:
        passport = input("Do you have a Golden Passport? (yes/no): ").lower()
        if passport == "no":
            print("Normal Rules")
        elif passport == "yes":
            print("Golden Passport\n")
            Age_first_person = 18
            Age_second_person = 18
            height_first_person = 62
            height_second_person = 62

elif second_rider == "no" and Age_first_person >= 12 and Age_first_person < 18:
    passport = input("Do you have a Golden Passport? (yes/no): ").lower()
    if passport == "no":
        Age_first_person = Age_first_person
        height_first_person = height_first_person
    elif passport == "yes":
        print("Golden Passport\n")
        Age_first_person = 18
        height_first_person = 62

# One Person
if second_rider == "no":
    if Age_first_person >= 18 and height_first_person >= 62:
        print("You can ride alone")
    elif height_first_person < 36:
        print("You can't ride")
    elif Age_first_person < 18 or height_first_person < 62:
        print("You can't ride")


# Second Person
elif second_rider == "yes":

    if height_first_person < 36 or height_second_person < 36:
        print("One of you don't have the minimal height")
    elif height_first_person >= 36 and height_second_person >= 36 and Age_first_person >= 18 or Age_second_person >= 18:
        print("Welcome to the ride. Please be safe and have fun!") 
    elif height_first_person >= 52 and height_second_person >= 52 and Age_first_person >= 12 and Age_second_person >= 12:
        print("Welcome to the ride. Please be safe and have fun!")
    elif Age_first_person >= 14 and Age_second_person >= 16 or Age_first_person >= 16 and Age_second_person >= 14:
        print("Welcome to the ride. Please be safe and have fun!")  

else:
    print("Try again")