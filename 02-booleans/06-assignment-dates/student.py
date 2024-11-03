# write your code here
def is_valid_month(month):
    if month >=1 and month <= 12:
        return True
    return False

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            return False
        return True
    return False

def has_30_days(month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return True
    return False

def has_31_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return True
    return False

def has_28_days(month, year):
    if month == 2 and is_leap_year(year) != True:
        return True
    return False

def has_29_days(month, year):
    if month == 2 and is_leap_year(year):
        return True
    return False

def is_valid_date(day, month, year):
    if is_valid_month(month) == True:
        if (has_31_days(month) == True and day >= 1 and day <= 31) or (has_30_days(month) == True and day >= 1 and day <= 30) or (has_28_days(month, year) == True and day >= 1 and day <= 28) or (has_29_days(month, year) == True and day >= 1 and day <= 29):
            return True
    return False