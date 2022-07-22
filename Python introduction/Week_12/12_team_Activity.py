# 12 Teach: Team Activity

max_number = -1
max_book = ""

with open("./Week_12/books_and_chapters.txt") as book:
    for line in book:
        parts = line.split(":")
        book = parts[0]
        number = parts[1]
        scripture = parts[2]

        number = int(number)

        if number > max_number:
            max_number = number
            max_book = book

print()
print(f"the book that has the largest number of chapters in the scriptures is {max_book} with {max_number} chapters")
