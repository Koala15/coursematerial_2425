def remove_backspaces(string):
    new_string = ""

    for char in string:
        if char == "\b":
            if len(new_string):
                new_string = new_string[0: len(new_string)-1]
        else:
            new_string += char
        
    
    return new_string
