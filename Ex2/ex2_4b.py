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