# write your code here
def split_name(full_name):
    space = full_name.find(" ")
    first_name = full_name[0:space]
    last_name = full_name[space+1:len(full_name)]

    return (first_name, last_name)
