# Wind Chill Calculations


user_temp = float(input("What is the temperature?: "))
temp_degree = input("Fahrenheit or Celsius (F/C): ").lower()
temp = int(0)

def wind_chill():
    for x in range(5,61,5):
        #print(x)
        formula = (35.74 + 0.6215*temp - 35.75*(x**0.16) + 0.4275*temp*(x**0.16))
        print(f"At temperature {user_temp}, and wind speed {x} mph, the windchill is:{round(formula,2)}F")


if temp_degree == "c":
    temp = (user_temp * 1.8) + 32
    wind_chill()

elif temp_degree == "f":
    temp = user_temp
    wind_chill()

else:
    print("Enter a correct letter (F/C)")

