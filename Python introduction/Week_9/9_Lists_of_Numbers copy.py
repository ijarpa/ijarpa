# Lists of Numbers

number_list = []
last_number = 1

while last_number != 0:
    last_number = int(input("Enter a number for the list: "))
    number_list.append(last_number)

print()
print(number_list)

print(f"SUM: {sum(number_list)}")
print(f"AVG: {round(sum(number_list)/len(number_list),2)}")
print(f"MAX: {max(number_list)}")

for x in number_list:
    if x > 0 and x < max(number_list):
        min_number = x
print(f"MIN: {min_number}")


number_list.sort()
print(number_list)






