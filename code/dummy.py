import datetime

def get_future_date(birthday, age):
    birthday_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    future_date = birthday_date + datetime.timedelta(years=age)
    return future_date
