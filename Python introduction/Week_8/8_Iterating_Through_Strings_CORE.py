# Iterating Through Strings

word = ("commitment")

favorite_letter = input("What is your favorite letter?: ").lower()

############ 1 Core Requirements ##############
for x in word:
    if favorite_letter == x:
        print(x.upper(), end="")
    else:
        print(x.lower(), end="")

############ 2 Core Requirements ##############
print()

for x in word:
    if favorite_letter == x:
        print("_", end="")
    else:
        print(x.lower(), end="")



