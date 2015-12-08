import sys
from birth_date import get_future_date, get_weekday


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
