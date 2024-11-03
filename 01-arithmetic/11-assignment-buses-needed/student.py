# write your code here
import math
from math import ceil

def buses_needed(people_count, bus_capacity):
    return math.ceil(people_count / bus_capacity)
