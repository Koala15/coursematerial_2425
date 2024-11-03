# write your code here
def is_capitalized(string):
    if len(string) == 0:
        return False
    elif string[0] >= "A" and string[0] <= "Z":
        x = string[1::1]
        l_string = x.lower()
        if l_string == x:
            return True
    return False