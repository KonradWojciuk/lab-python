import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def main():
    shape = input("Enter the name of the shape (rectangle, triangle, circle): ").lower()
    
    if shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        if length > 0 and width > 0:
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle is: {area}")
        else:
            print("Invalid input. Length and width must be greater than 0.")
    
    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        if base > 0 and height > 0:
            area = calculate_triangle_area(base, height)
            print(f"The area of the triangle is: {area}")
        else:
            print("Invalid input. Base and height must be greater than 0.")
    
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        if radius > 0:
            area = calculate_circle_area(radius)
            print(f"The area of the circle is: {area}")
        else:
            print("Invalid input. Radius must be greater than 0.")
    
    else:
        print("Invalid shape. Please enter rectangle, triangle, or circle.")

if __name__ == "__main__":
    main()
