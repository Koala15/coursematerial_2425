# write your code here
import math

def middle(a, b, c):
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    som = a + b + c
    return som - minimum - maximum

"""def middle(a, b, c):
    return max(min(a, b), c)"""