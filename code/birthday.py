import sys
import settings
from birth_date import BirthdayDate


def main():
    age = sys.argv[1]
    try:
        age = int(age)
    except ValueError:
        print("ERROR: Please provide an integer")
        return

    if age < 0:
        print("ERROR: Negative ages are not possible")
        return
    if age >= 0:
        bdate = BirthdayDate(settings.BIRTHDAY)
        future_date = bdate.get_future_date(age)
        weekday = bdate.get_birthday_weekday(age)
        message = "You will turn {} on {}, {}".format(
            age, weekday, future_date)
        print(message)

main()
