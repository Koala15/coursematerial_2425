# write your code here
def box(string):
    line = "-" * (len(string) + 2)
    return f"+{line}+\n| {string} |\n+{line}+"