import csv
import random
import webbrowser
import statistics

def lego_database(year, csv_file):
    sets_count = 0
    pieces_count = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['year']) == year:
                sets_count += 1
                pieces_count.append(int(row['num_parts']))

    if sets_count == 0:
        print("Brak zestawów z podanego roku.")
    else:
        print(f"Ilość zestawów z roku {year}: {sets_count}")
        print(f"Średnia ilość elementów w zestawach: {statistics.mean(pieces_count)}")
        print(f"Mediana ilości elementów w zestawach: {statistics.median(pieces_count)}")

        # Losowanie i wyświetlenie zdjęcia zestawu
        random_set = random.choice(list(pieces_count))
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['num_parts']) == random_set:
                    webbrowser.open(row['img_url'])
                    break

def main():
    lego_database(2022, 'D:\Projects\python\Cw3\sets.csv')

if __name__ == "__main__":
    main()