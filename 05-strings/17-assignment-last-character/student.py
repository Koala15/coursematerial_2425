# write your code here

def last_character(string):
    if string == "":
        return None
    else:
        index_last = len(string) -1
        last_car = string[index_last]
        return last_car
