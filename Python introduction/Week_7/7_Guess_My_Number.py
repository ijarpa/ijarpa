import random

game = 0

games = [1]


number = random.randint(1, 100)

while game != number:

    guess_number = int(input("What is the magic number?: "))

    if guess_number < number:
        print("Higher")
        games.append(1)
    elif guess_number > number:
        print("Lower")
        games.append(1)
    else:
        print("You guessed it!")
        print(f"You guessed with {len(games)} tries")
        
        game_again = input("Do you want to game again? (yes/no): ").lower()
        if game_again == "yes":
            number = random.randint(1, 100)
            games = [1]
            game = 0
        else:
            print("Thank you for playing!")
            game = number

