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