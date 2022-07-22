# Milestone - Adventure Game

# scenerio 1 princess rescue
print("Hi User welcome to Milestone Adventure Game")
print("""
the objective is princess rescue from a dragon cave, 
so you need to choose a weapon
""")

waepon = []
result = []
place_to_fight = []

choice_1 = int(input("""Pick the number of your weapon: 
1: Spear
2: Sword
3: Magic

number:
"""))

print()

choice_2 = int(input("""Pick the number of the place to fight: 
1: Mountains
2: Woods

number:
"""))

print()

if choice_1 == 1 and choice_2 ==1 :
    weapon = "Spear"
    place_to_fight = "Mountains"
    result = "You can only fight far of the dragon, and in the Mountains the dragon have advantage"
elif choice_1 == 1 and choice_2 ==2 :
    weapon = "Spear"
    place_to_fight = "Woods"
    result = "You can only fight far of the dragon, if the dragon is close to you, you will be in danger"    
elif choice_1 == 2 and choice_2 == 1:
    weapon = "Sword"
    place_to_fight = "Mountains"
    result = "You have the advantage againts the dragon!"
elif choice_1 == 2 and choice_2 == 2:
    weapon = "Sword"
    place_to_fight = "Woods"
    result = "It is too dangerous for you the woods!"
elif choice_1 == 3:
    weapon = "Magic"
    result = "The magic does not affect the dragon, you need to run out"
else:
    print("Choose a correct number!")

print()



print(f"You chose {weapon} and the place to fight againts the dragon is {place_to_fight}!! {result}")


