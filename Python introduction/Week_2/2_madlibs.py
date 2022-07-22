print("############### MAD LIBS ###############\n")

print("Hi user! to play enter the following words:\n")
adjective = input("adjective:")
animal = input("animal:")
verb_1 = input("verb:")
exclamation = input("exclamation:")
verb_2 = input("verb:")
verb_3 = input("verb:")

a_an = []

vowels = ["a","e","i","o","u"]

if adjective[0].lower() in(vowels):
    a_an = "an"
else:
    a_an = "a"

print(f"""
The other day, I was really in trouble. It all started when I saw {a_an}
{adjective} {animal} {verb_1} down the hallway. "{exclamation.capitalize()}!" I yelled. 
But all I could think to do was to {verb_2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb_3} right in front
of my family.
""")