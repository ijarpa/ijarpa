# Milestone - Adventure Game

# scenerio 1 princess rescue
print("Hi User welcome to Milestone Adventure Game")
print("""
the objective is princess rescue from a Dragon cave, 
so you need to choose a weapon
""")

game = 0

while game == 0:
    print("Prepare to fight against the Dragon!")
    weapon = input("What kind of weapon will you use?: (Sword/ Magic) ").capitalize()
    armor = input("Which Armor will you use?: (Chain armor/ Magic cape/ Bear skin) ").capitalize()
    print("\n################ ################\n")
    if weapon == "Sword":
        if armor == "Chain armor":
            print("Great selection! You have all the chance to win!")
            game = 1
        elif armor == "Magic cape":
            print("Those components don't work very good together! Be careful")
            game = 1
        elif armor == "Bear skin":
            print("You look awesome! but take care of the Dragon")
            game = 1
        else:
            print("wrong answer, try again\n")
            game = 0

    elif weapon == "Magic":
        if armor == "Magic cape":
            print("Great selection! with the cape your Magic power will be increased!")
            game = 1
        elif armor == "Chain armor":
            print("Your magic need a better armor to work properly")
            game = 1
        elif armor == "Bear skin":
            print("You look awesome! but take care of the Dragon")
            game = 1
        else:
            print("wrong answer, try again\n")
            game = 0
    
    else:
        print("You need to enter a correct answer, try again.")
        game = 0

