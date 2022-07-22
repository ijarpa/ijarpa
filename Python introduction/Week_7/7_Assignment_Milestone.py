# Assignment Milestone
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

while game != secret_word:
    print(f"The secret word has {letters} letters)")
    guess = input("What is your guess?: ").capitalize()
    tries += 1
    if guess != secret_word:
        print("Your guess was not correct.")
    else:
        print("Congratulations! You guessed it!")
        print(tries)
        game = secret_word