# write your code here

def fix_date(date):
    day = date[3:5]
    month = date[0:2]
    year = date[6:10]
    new_date = f"{year}/{month}/{day}"
    return new_date