import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def get_shape():
    while True:
        shape = input("Enter the name of shape (rectangle, triangle, circle), or type 'stop' to exit: ")
        if shape in ["rectangle", "triangle", "circle", "stop"]:
            return shape
        else:
            print("Invalid shape. Please enter rectangle, triangle, circle, or stop.")

def get_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Invalid input. Number must be grater than 0.")
        except:
            print("Invalid input. Please enter the number.")

def calculate_and_print_rectangle_area():
    length = get_positive_number("Enter the length of rectangle: ")
    width = get_positive_number("Enter the width of rectangle: ")
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")

def calculate_and_print_triangle_area():
    base = get_positive_number("Enter the base of triangle: ")
    height = get_positive_number("Enter the height of triangle: ")
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle is: {area}")

def calculate_and_print_circle_area():
    radius = get_positive_number("Enter the radius of triangle: ")
    area = calculate_circle_area(radius)
    print(f"The area of the circle is: {area}")

def main():
    while True:
        shape = get_shape()
        if shape == "stop":
            break
        elif shape == "rectangle":
            calculate_and_print_rectangle_area()
        elif shape == "triangle":
            calculate_and_print_triangle_area()
        elif shape == "circle":
            calculate_and_print_circle_area()

if __name__ == '__main__':
    main()  