def group_by_first_letter(strings):
    my_dict = dict()

    for s in strings:
        if len(s):
            letter = s[0].upper()
            words = my_dict.get(letter, [])
            words.append(s)
            my_dict[letter] = words

    return my_dict