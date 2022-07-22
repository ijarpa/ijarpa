# Lists of Numbers

import numpy as np

number_list = []
last_number = 1

while last_number != 0:
    last_number = int(input("Enter a number for the list: "))
    number_list.append(last_number)

print(number_list)

data = np.array(number_list)

# Results
print(f"SUM: {data.sum()}")
print(f"AVERAGE: {data.mean()}")
print(f"MAX: {data.max()}")

# Min positive number
for x in number_list:
    if x > 0 and x < max(number_list):
        min_number = x
print(f"MIN: {min_number}")


print(np.sort(data))