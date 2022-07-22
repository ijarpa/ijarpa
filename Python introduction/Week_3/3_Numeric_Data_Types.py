import math
pi = math.pi
print("Areas of Shapes\n")

x_square = int(input("What is the length of a side of the square?: "))
square_area = (x_square*x_square)
print(f"The area of the square is:",square_area)

x_rectangle = int(input("What is the length of rectangle?: "))
y_rectangle = int(input("What is the width of the rectangle?: "))
rectangle_area = (x_rectangle*y_rectangle)
print(f"The area of the rectangle is:",rectangle_area)

x_circle = int(input("What is the radius of the circle?: "))
circle_area = round(pi*x_circle,2)
print(f"The area of the circle is:",circle_area)

##### single length value #####
print()
single_value = int(input("Write a single length value: "))
square_single = round((single_value*single_value),2)
circle_single = round((pi*single_value),2)
cube_single = round((single_value*single_value*single_value),2)
print(f"The area of the square is:",square_single)
print(f"The area of the circle is:",circle_single)
print(f"The volume of the cube is:",cube_single)

##### value in centimeters #####
print()
x_square = int(input("What is the length in cm of a side of the square?: "))
square_area = round((x_square*x_square),2)
print(f"The area of the square in cm2 is:",square_area)
print(f"The area of the square in m2 is:",square_area/10000)

x_rectangle = int(input("What is the length in cm of rectangle?: "))
y_rectangle = int(input("What is the width in cm of the rectangle?: "))
rectangle_area = round((x_rectangle*y_rectangle),2)
print(f"The area of the rectangle in cm2 is:",rectangle_area)
print(f"The area of the rectangle in m2 is:",rectangle_area/10000)

x_circle = int(input("What is the radius in cm of the circle?: "))
circle_area = round(pi*x_circle,2)
print(f"The area of the circle in cm2 is:",circle_area)
print(f"The area of the circle in m2 is:",circle_area/10000)