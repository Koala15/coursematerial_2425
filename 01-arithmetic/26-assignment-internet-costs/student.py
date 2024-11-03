# write your code here
import math
from math import ceil

def internet_costs(duration_in_seconds, cost_per_block):
    block = 6 * 60
    count_block = math.ceil(duration_in_seconds / block)
    return count_block * cost_per_block