import datetime
import sys


BIRTHDAY = "1982-09-08"


def get_future_date(age):
    date_object = datetime.datetime.strptime(BIRTHDAY, '%Y-%m-%d')
    future_date = datetime.date(
        date_object.year + age,
        date_object.month,
        date_object.day
    )
    return future_date


def get_weekday(weekday_number):
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return weekdays[weekday_number - 1]


def main():
    age = None
    try:
        age = int(sys.argv[1])
    except ValueError:
        print("ERROR: Please enter an integer")
        return

    if age < 0:
        print("ERROR: Negative ages are not allowed")
        return
    else:
        future_date = get_future_date(age)
        weekday = get_weekday(future_date.isoweekday())
        message = "I will turn {} on {}, {}".format(age, weekday, future_date)
        print(message)

main()
