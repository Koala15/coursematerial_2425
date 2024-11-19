# write your code here
def heatwave(temperatures):
    if len(temperatures) < 5:
        return False
    
    over_25 = 0
    over_30 = 0
    for temp in temperatures:
        if temp >= 25:
            over_25 +=1
            if temp >=30:
                over_30 +=1
        else:
            over_25 = 0
            over_30 = 0
        if over_25 >=5 and over_30 >=3:
            return True
    return False