# write your code here
def increasing(ns):
    if len(ns) <= 1:
        return True
    
    for i in range(0, len(ns)-1):
        if ns[i] > ns[i+1]:
            return False
        
    return True