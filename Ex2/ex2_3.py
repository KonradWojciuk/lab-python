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