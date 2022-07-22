# team activity
area = -1

from math import pi

def square_area(square_side):
    return square_side * square_side

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return pi * (radius * radius)

while area != 0:
    print("""
1 - Square
2 - Rectangle
3 - Circle
0 - Quit
\n""")
    area = int(input("Type the number of the shape that you want to calculate: "))

    if area == 1:
        square_side = float(input("Enter the length of the side: "))
        print(f"The area of the square is: {square_area(square_side)}")
        move_on = input("Press enter to continue")
    
    elif area == 2:
        length_side = float(input("Enter the length of the rectangle: "))
        width_side = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area_rectangle(length_side, width_side)}")
        move_on = input("Press enter to continue")

    elif area == 3:
        radius = float(input("Enter the radius of the circle: "))

        print(f"The area of the circle is: {area_circle(radius):.2f}")
        move_on = input("Press enter to continue")
