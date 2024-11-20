def find_duplicates(xs):
    current_set = set()             # keeps the items ia have parsed so far, no duplicates
    new_set = set()

    for x in xs:
        if (len(current_set) > 0) and (x in current_set):        # if it was at least one appearance
            new_set.add(x)                                  # add it to the result list
        else:                                                   # else add it to the parsed set
            current_set.add(x)
    return list(new_set)
