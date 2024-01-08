def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    days = []
    if is_year_leap(year):
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]


def day_of_year(year, month, day):
    print("Year=", 2000, "Month=", 12, "Day=", 31)
    total_days = 0

    if is_year_leap(year):
        total_days = 366
    else:
        total_days = 365

    print('Total days in year=', total_days)

    sum = 0
    for i in range(1, month):
        days_for_month = days_in_month(year, i)
        print("Month:", i, "has", days_for_month, "days.")
        sum += days_for_month
        print(i, sum)
    sum += day
    return sum

def fun(in=2,out=3):
    return in * out




print(day_of_year(2000, 12, 31))
