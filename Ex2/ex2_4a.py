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