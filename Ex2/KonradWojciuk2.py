# Ex.1

def main():
    products = input("Wprowadź produkty oddzielone przecinkiem: ")

    product_list = products.split(",")
    
    cash_register = {}

    for product in product_list:
        product = product.strip().lower()

        price = float(input(f"Podaj cenę produktu {product}: "))

        cash_register[product] = price

    for product, price in cash_register.items():
        print(f"{product}: {price:.2f} zł")

if __name__ == "__main__":
    main()

# Ex.2

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

# Ex.3

def validate_pesel(pesel):
    if len(pesel) != 11:
        return False, "Nieprawidłowa długość numeru PESEL"
    
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month in range(21, 33):
        month -= 20

    if month < 1 or month > 12:
        return False, "Nieprawidłowy miesiąc urodzenia"
    if day < 1 or day > 31:
        return False, "Nieprawidłowy dzień urodzenia"
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    
    if day > max_day:
        return False, "Nieprawidłowy dzień w miesiącu urodzenia"
    
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_check = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (sum_check % 10)) % 10

    if control_digit != int(pesel[10]):
        return False, "Niepoprawna cyfra kontrolna numeru PESEL"
    
    if year < 0 or year > 99:
        return False, "Niepoprawny rok urodzenia"
    
    return True, None

def parse_pesel(pesel):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if year < 20:
        year += 2000
    else:
        year += 1900

    if year > 2000:
        month -= 20

    gender_digit = int(pesel[9])
    gender = "mężczyzna" if gender_digit % 2 == 1 else "kobieta"

    return f"Data urodzenia: {day:02}.{month:02}.{year}, {gender}"

def main():
    pesel_input = input("Podaj numer PESEL: ")

    valid, messeage = validate_pesel(pesel_input)

    if valid:
        print("Numer PESEL jest poprawny")
        print(parse_pesel(pesel_input))
    else:
        print(f"Numer PESEL jest niepoprawny: {messeage}")

if __name__ == "__main__":
    main()

# Ex.4

import math

# a) Obliczanie pola trójkąta za pomocą wzoru Herona

def calculate_triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        area = round(area, 2)     
        return area
    else:
        return -1

def main():
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))

    result = calculate_triangle_area(a, b, c)
    if result == -1:
        print("Nie można zbudować trójkąta o podanych bokach")
    else:
       print(f"Pole trójkąta wynosi {result}")

if __name__ == "__main__":
    main()

# b) Obliczanie pierwiastków równania kwadratowego

def calculate_quadratic_roots(a, b, c):
    delta = b**2 - 4*a*c
    print(f"Delta: {delta}")

    if delta >= 0:
        x1 = (-b + delta ** 0.5) / (2*a)
        x2 = (-b - delta ** 0.5) / (2*a)
        return x1, x2
    else:
        return None 

def main():
    a = float(input("Podaj wartość parametru a: "))
    b = float(input("Podaj wartość parametru b: "))
    c = float(input("Podaj wartość parametru c: "))

    roots = calculate_quadratic_roots(a, b, c)
    if roots:
        print(f"Pierwiastki równania to: {roots[0]} i {roots[1]}")
    else:
        print("Brak pierwiastków rzeczywistych dla podanych parametrów.")

if __name__ == "__main__":
    main()

# Ex.5

# a) Iteracyjnie:

def draw_triangle_itereatively(n):
    for i in range(1, n + 1):
        print(i * "*")

# b) Rekurencyjnie:
def draw_triangle_recursive(levels, current_level=1):
    if current_level <= levels:
        print('*' * current_level)
        draw_triangle_recursive(levels, current_level + 1)

def main():
    levels = int(input("Podaj liczbę poziomów trójkąta dla iteracji: "))
    draw_triangle_itereatively(levels)
    levels = int(input("Podaj liczbę poziomów trójkąta dla rekurencji: "))
    draw_triangle_recursive(levels)

if __name__ == "__main__":
    main()