wydatki = {
    "styczeń": 2500,
    "luty": 2800,
    "marzec": 3000,
    "kwiecień": 2700,
    "maj": 3200
}

# Wartość minimalna
minimalna_wartosc = min(wydatki.values())

# Wartość maksymalna
maksymalna_wartosc = max(wydatki.values())

# Suma wartości
suma_wartosci = sum(wydatki.values())

# Wartość średnia
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