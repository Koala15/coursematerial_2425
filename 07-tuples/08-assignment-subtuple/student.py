# write your code here
def subtuple(xs, ys):
    if len(ys) == 0:
        return True
    if len(xs) <= 0 or len(xs) < len(ys):
        return False
    
    for i in range (0, len(xs) - len(ys) + 1 ):
        if xs[i] == ys[0]:
            for j in range (0, len(ys)):
                if xs[i+j] != ys[j]:
                    return False
            return True
    return False