# write your code here
import math
from math import ceil

def base_price(duration):
    if duration < 90:
        return 10
    elif duration >= 90 and duration < 120:
        return 11
    elif duration >= 120 and duration < 150:
        return 12
    else:
        return 15

def movie_ticket(duration, imax, student, ticket_count):
    price = base_price(duration)

    if imax:
        price = ceil(price * 1.2 )
    
    if student:
        price = price - 3
    
    return price * ticket_count