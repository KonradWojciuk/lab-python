# Ex 1
import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))


print(f"Cześć {name}!")
print(f"Twoje imię ma {len(name)} liter i zaczyna się od {name[0]}.")
print(f"Teraz masz {age} lat, a za rok będzie to {age + 1}. Rok urodzenia to {datetime.datetime.now().year - age}.")

# Ex 2
age = input("Enter your age: ")
money = input("Enter your money: ")

if int(age) >= 18 and int(money) > 20:
    print("You can buy a vodka")
elif int(age) >= 18 and int(money) < 20:
    print("You have not enough money but your age is ok")
elif int(age) < 18 and int(money) > 20:
    print("You have not enough age but your money is ok")
elif int(age) < 18 and int(money) < 20:
    print("You have not enough age and money")

# Ex 3
def calculate_tax(income):
    if income <= 50000:
        tax = income * 0.12
    else:
        tax = 50000 * 0.12 + (income - 50000) * 0.32
    return tax

def main():
    income_type = input("Enter 'M' for monthly income or 'Y' for yearly income: ")
    if income_type.upper() == 'M':
        monthly_income = float(input("Enter your monthly income: "))
        yearly_income = monthly_income * 12
    elif income_type.upper() == 'Y':
        yearly_income = float(input("Enter your yearly income: "))
    else:
        print("Invalid input. Please enter 'M' or 'Y'.")
        return
    
    tax_amount = calculate_tax(yearly_income)
    print("Your yearly income tax is:", tax_amount)

if __name__ == "__main__":
    main()

# Ex 4
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

# Ex 5
wydatki = {
    "styczeń": 2500,
    "luty": 2800,
    "marzec": 3000,
    "kwiecień": 2700,
    "maj": 3200
}

minimalna_wartosc = min(wydatki.values())

maksymalna_wartosc = max(wydatki.values())

suma_wartosci = sum(wydatki.values())


srednia_wartosci = suma_wartosci / len(wydatki)

print(f"Wartość minimalna: {minimalna_wartosc}")
print(f"Wartość maksymalna: {maksymalna_wartosc}")
print(f"Suma wartości: {suma_wartosci}")
print(f"Wartość średnia: {srednia_wartosci}")

if wydatki["maj"] > srednia_wartosci:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")

print("Wydatki przekraczające średnią:")
for miesiac, wydatek in wydatki.items():
    if wydatek > srednia_wartosci:
        print(f"{miesiac}: {wydatek}")