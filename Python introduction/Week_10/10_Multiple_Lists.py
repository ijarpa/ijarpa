# Multiple Lists

checking = []
saving = []

bank = 0 

while bank != 1:
    
    accounts = input("What is the name of this account?:")
    checking.append(accounts)
    balance = float(input("What is the balance?:"))
    saving.append(balance)

    ask = input("do you want to add another account?: yes/no ").lower()
    if ask == "yes":
        bank = 0
    else:
        bank = 1

print("\nAccount Information:\n")
for x in range(len(checking)):
    list_1 = checking[x]
    list_2 = saving[x]
    print(f"{list_1} - ${list_2}")

print()

print(f"Total: {sum(saving)}")
print(f"Average: {round(sum(saving)/len(saving),2)}")
