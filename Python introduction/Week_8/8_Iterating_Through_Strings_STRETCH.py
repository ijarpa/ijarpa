# Iterating Through Strings Stretch Challenge

quote = ("In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.").lower()

#number = input("Please enter a number: ")
# % = Modulus

number = int(input("Please enter a number: "))

for x, quote in enumerate(quote):
    if (x%number)==0:
        print(quote.capitalize(), end="")
    else:
        print(quote.lower(), end="")



