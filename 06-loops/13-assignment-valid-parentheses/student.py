def valid_parentheses(string):
    open_p = 0
    closed_p = 0
    lenght = len(string)

    if lenght % 2 == 1:
        return False
    
    if string == "":
        return True
    
    for char in string:
        if char == "(":
            open_p += 1
        elif char == ")":
            closed_p +=1
            if closed_p > open_p:
                return False
    return open_p == closed_p
        

