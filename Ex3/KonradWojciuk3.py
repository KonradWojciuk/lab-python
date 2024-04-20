# Ex.1
import os
import shutil
ph =r'.'

list_files_log =[]
new_folder_name = os.path.join(ph, 'kopie')
os.makedirs(new_folder_name,exist_ok = True) 

for folder in os.listdir(ph):
    folder_address=os.path.join(ph, folder)
    if os.path.isdir(folder_address):
        list_files_log.append(folder_address)
        counter = 0 
        for  file in os.listdir(folder_address):
            extension = file.split('.').pop().upper()
            if extension in ('JPG', 'PNG'):
                original_address = os.path.join(folder_address,file)
                new_file_address = os.path.join(new_folder_name, folder.upper() + str(counter) +'.' + extension)
                # shutil.copy(src=original_address, dst=new_file_address)
                print(original_address, new_file_address)
                list_files_log.append(file)
                counter+=1

log_file = r'log.txt'
with open(log_file,'w') as tfile:
	tfile.write('\n'.join(log_file))

# Ex.2
import smtplib
from email.message import EmailMessage

def read_config(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split("=")
            config[key.strip()] = value.strip()
    return config

def send_email(sender_email, sender_password, receiver_email, subject, message):
    msg = EmailMessage()
    msg['from'] = sender_email
    msg['to'] = receiver_email
    msg['subject'] = subject
    msg.set_content(message)
    

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()

    server.login(sender_email, sender_password)

    server.send_message(msg)

    server.quit()

def main():
    file_data = read_config('D:\Projects\python\Cw3\data.txt')

    sender_email = file_data['sender_email']
    sender_password = file_data['sender_password']
    recipient_email = file_data['recipient_email']
    subject = file_data['subject']
    text = file_data['text']
    send_email(sender_email, sender_password, recipient_email, subject, text)


if __name__ == "__main__":
    main()

# Ex.3
import datetime
import calendar

def payday_calendar(year):
    for month in range(1, 13):
        last_day = max(1, calendar.monthrange(year, month)[1])
        date = datetime.date(year, month, last_day)
        while date.weekday() > 4:
            date -= datetime.timedelta(days=1)
        
        print(f"{calendar.month_name[month]}: {date.strftime('%d-%m-%Y')}")

def main():
    payday_calendar(2024)

if __name__ == "__main__":
    main()

# Ex.4
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
    lego_database(2020, 'D:\Projects\python\Cw3\sets.csv')

if __name__ == "__main__":
    main()