def plagiarism(s1, s2):
    s1_lines = set(s1.split("\n"))      # all the different lines in s1 without duplicates
    s2_lines = set(s2.split("\n"))      # all the different lines in s2 without duplicates

    return len(s1_lines & s2_lines)     # the number of common lines in s1 and s2 without duplicates