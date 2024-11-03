# write your code here
def is_digit(char):
    if ("0"<= char[0]) and (char[0] <= "9") and ("0"<= char[1]) and (char[1] <= "9") and ("0"<= char[2]) and (char[2] <= "9") and ("0"<= char[3]) and (char[3] <= "9") and ("0"<= char[4]) and (char[4] <= "9") and ("0"<= char[5]) and (char[5] <= "9") and ("0"<= char[6]) and (char[6] <= "9"):
        return True
    return False

def is_student_id(string):
    x = string[0]
    if len(string) == 8:
        if (x == "R") or (x == "r") or (x == "S") or (x == "s"):
            char = string[1:]
            if is_digit(char) == True:
                return True
    return False
