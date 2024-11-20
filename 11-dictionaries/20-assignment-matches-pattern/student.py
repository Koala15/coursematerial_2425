# write your code here
def matches_pattern(pattern, string):
    if len(pattern) != len(string):
        return False
    
    d_pattern = dict()   # dictionary {pattern:string}
    d_string = dict()    # dictionary {string:pattern}

    for index in range(len(pattern)):
        key_pattern = pattern[index]
        key_string = string[index]

        if key_pattern in d_pattern:
            if d_pattern[key_pattern] != key_string:
                return False
        else:
            d_pattern[key_pattern] = key_string

        if key_string in d_string:
            if d_string[key_string] != key_pattern:
                return False
        else:
            d_string[key_string] = key_pattern

    return True
            
