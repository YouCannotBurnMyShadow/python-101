from datetime import date, datetime


class BirthdayDate(object):
    date_of_birth = None

    def __init__(self, date_string):
        self.date_of_birth = date_string

    def get_future_date(self, age):
        date_object = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        future_date = date(
            date_object.year + int(age),
            date_object.month,
            date_object.day
        )
        return future_date

    def get_weekday_string(self, weekday_number):
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

    def get_birthday_weekday(self, age):
        future_date = self.get_future_date(age)
        weekday_number = future_date.isoweekday()
        return self.get_weekday_string(weekday_number)
