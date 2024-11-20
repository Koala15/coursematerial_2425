def remove_duplicates(xs):
    new_list = list()
    new_set = set()
    for x in xs:
        if len(new_list) == 0:
            new_list.append(x)
            new_set.add(x)
        elif not (x in new_set):
            new_list.append(x)
            new_set.add(x)

    return new_list