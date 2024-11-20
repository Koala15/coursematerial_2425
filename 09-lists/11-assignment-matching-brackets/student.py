def matching_brackets(string):
    if len(string) == 0:    # if empty string
        return True
    if len(string) % 2:     # if odd length string
        return False
    
    new_string = []            # we append and pop corresponding parathesis

    for i in string:
        if i == "(" or i == "{" or i == "[" or len(new_string) == 0:
            new_string.append(i)
        elif new_string[len(new_string)-1] == "(" and i == ")":
            new_string.pop()
        elif new_string[len(new_string)-1] == "{" and i == "}":
            new_string.pop()
        elif new_string[len(new_string)-1] == "[" and i == "]":
            new_string.pop()
        else:
            return False
        
    return len(new_string) == 0
