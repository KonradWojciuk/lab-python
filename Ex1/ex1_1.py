import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))


print(f"Cześć {name}!")
print(f"Twoje imię ma {len(name)} liter i zaczyna się od {name[0]}.")
print(f"Teraz masz {age} lat, a za rok będzie to {age + 1}. Rok urodzenia to {datetime.datetime.now().year - age}.")