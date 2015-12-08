import sys
import settings
from birth_date import BirthdayDate


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
        bday = BirthdayDate(settings.BIRTHDAY)
        future_date = bday.get_future_date(age)
        weekday = bday.get_birthday_weekday(age)
        message = "I will turn {} on {}, {}".format(age, weekday, future_date)
        print(message)

main()
