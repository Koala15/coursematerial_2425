# write your code here
import math

def hours(duration):
    return duration // 3600

def minutes(duration):
    h = hours(duration)
    rest = duration - (3600 * h)
    return  rest // 60

def seconds(duration):
    h = hours(duration)
    m = minutes(duration)
    rest = duration - (3600 * h) -(60 * m)

    return  rest
