# write your code here
def empty_seats(used_seats):
    if len(used_seats) <=1:
        return 0
    first = min(used_seats)
    last  = max (used_seats)
    return last - first - len(used_seats) + 1