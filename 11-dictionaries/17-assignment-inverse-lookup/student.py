def inverse_lookup(dictionary, value):
    my_keys = []
    for key in dictionary.keys():
        if dictionary[key] == value:
            my_keys.append(key)
    return my_keys
