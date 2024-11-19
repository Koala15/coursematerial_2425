# write your code here
def all_equal(xs):
    if len(xs) <= 1:
        return True
    
    for i in range(0, len(xs)-1):
        if xs[i] != xs[i+1]:
            return False
        
    return True