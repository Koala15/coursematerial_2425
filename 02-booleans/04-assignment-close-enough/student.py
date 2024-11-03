# write your code here
def close_enough(x, y):
    if x > y and x - y <= 0.1:
        return True
    elif x < y and y - x <= 0.1:
        return True
    elif x==y:
        return True
    else:
        return False