# Assignment Milestone
from ast import IsNot
import random

books = ["First Nephi",
    "Second Nephi",
    "Jacob",
    "Enos",
    "Jarom",
    "Omni",
    "Words of Mormon",
    "Mosiah",
    "Alma",
    "Helaman",
    "Third Nephi",
    "Fourth Nephi",
    "Mormon",
    "Ether",
    "Moroni"]

chosen_number = random.randint(0, 14)

print("Welcome to the word guessing game!")
print("The words are books of The Book of Mormon")

secret_word = books[chosen_number].capitalize()

letters = len(secret_word)
game = "off"
tries = 0

hint = []

for x in range(len(secret_word)):
    hint.append("_")



while game != secret_word:

    print(' '.join(hint))  
    print(f"\nThe secret word has {letters} letters)")


    guess = input("\nWhat is your guess?: ").capitalize()
    tries += 1
    

    if guess != secret_word:

        # Code option #1
        for i, x in enumerate(guess):
            if x in secret_word and x == secret_word[i]:
                print(x.upper(), end=" ")
            elif x in secret_word and x != secret_word[i]:
                print(x.lower(), end=" ")
            else:
                print("_ ", end=" ")

        # Code option #2
        #for x in guess:
        #    if x in secret_word:
        #        for i in range(0, len(secret_word)):
        #            if secret_word[i] == x:
        #                hint[i] = x.upper()
        
            
    else:
        print("Congratulations! You guessed the secret word!")
        print(f"Your tries were: {tries}")
        game = secret_word
