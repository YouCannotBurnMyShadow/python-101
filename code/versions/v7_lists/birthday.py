import sys
BIRTHDAY = "1982-09-08"


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
        message = "I am born {} and I am {} years old".format(BIRTHDAY, age)
        print(message)

main()
print(get_weekday(1))
