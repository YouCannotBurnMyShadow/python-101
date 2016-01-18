from datetime import date, datetime
import settings


def get_future_date(age):
    date_object = datetime.strptime(settings.BIRTHDAY, '%Y-%m-%d')
    future_date = date(
        date_object.year + int(age),
        date_object.month,
        date_object.day
    )
    return future_date


def get_weekday(weekday_number):
    weekdays = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ]
    return weekdays[weekday_number - 1]
