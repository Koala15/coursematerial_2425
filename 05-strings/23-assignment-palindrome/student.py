# write your code here

def palindrome(string):
    #len_string = len(string) - 1
    backwards = string[::-1]

    if backwards == string:
        return True
    return False