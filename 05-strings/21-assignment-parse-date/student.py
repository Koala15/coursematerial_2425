# write your code here

def parse_day(string):
    x = string[0:2]
    if x[0] == "0":
        day = int(x[1])
        return day
    else:
        day = int(x)
        return day

def parse_month(string):
    y = string[3:5]
    if y[0] == "0":
        month = int(y[1])
        return month
    else:
        month = int(y)
        return month

def parse_year(string):
    year = int(string[6:])
    return year