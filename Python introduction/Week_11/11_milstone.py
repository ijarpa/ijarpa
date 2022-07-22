# 11 Prove: Assignment Milestone

# create the lists
country_name = []
country_id = []
year_list = []
life_expectancy = []

with open("./Week_11/life-expectancy.csv") as data_life:
    for line in data_life:

        line = line.strip('/n')
        lines_parts = line.split(",")

        country_name.append(lines_parts[0])
        country_id.append(lines_parts[1])
        year_list.append(lines_parts[2])
        life_expectancy.append(lines_parts[3])

# remove the firt rows
country_name.pop(0)
country_id.pop(0)
year_list.pop(0)
life_expectancy.pop(0)

# convert the list to int and float
year_list = [int(item) for item in year_list]
life_expectancy = [float(item) for item in life_expectancy]

# Assignment
# min value for life expectancy
print("Milestone Requirements \n")
min_life = min(life_expectancy)
print(f"The overall min life expectancy is: {min_life:.2f}")

# max value for life expectancy
max_life = max(life_expectancy)
print(f"The overall max life expectancy is: {max_life:.2f} \n")


# Showing Creativity and Exceeding Requirements
user_life_expectancy = []
largest_drop = []

print("Exceeding Requirements \n")
user_country = input("Enter a country of your interest: ")

for x in range(0, len(country_name)):
    country_2 = country_name[x]
    year_2 = year_list[x]
    life_expectancy_2 = life_expectancy[x]
    
    if user_country == country_2:
        
        user_life_expectancy.append(life_expectancy_2)

print(f"The minimum life expectancy for {user_country} is: {min(user_life_expectancy)}")
print(f"The maximum life expectancy for {user_country} is: {max(user_life_expectancy)}")
