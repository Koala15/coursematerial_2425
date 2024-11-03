# write your code here


def parse_position_x(string):
    comma_p = string.find(",")
    open_h = string.find("(")

    if comma_p > -1:
        if open_h > -1:
            x = string[open_h+1:comma_p]
            return float(x)
        else:
            x = string[0:comma_p]
            return float(x)
    return 0
    
def parse_position_y(string):
    comma_p = string.find(",")
    end_h = string.find(")")

    if comma_p > -1:
        if end_h > -1:
            x = string[comma_p+1:end_h]
            return float(x)
        else:
            x = string[comma_p:]
            return float(x)
    return 0
