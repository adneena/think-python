import datetime

import datetime


def print_date_and_day_of_week():
    date = datetime.date.today()

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = days_of_week[date.weekday()]
    print(date, " : ", day_of_week)


def time_to_next_birthday(birth_year, birth_month, birth_day):
    birth = datetime.datetime(birth_year, birth_month, birth_day)
    current_time = datetime.datetime.now()

    current_age = current_time.year - birth.year - ((current_time.month, current_time.day) < (birth.month, birth.day))

    if (current_time.month, current_time.day) < (birth.month, birth.day):
        next_bday = (current_time.year, birth_month, birth_day)
    else:
        next_bday = (current_time.year + 1, birth_month, birth_day)

    time_to_next_bday = datetime.datetime(*next_bday) - current_time

    print("current age: ", current_age)
    print("time to next birthday: ", time_to_next_bday)


time_to_next_birthday(1997, 8, 23)
