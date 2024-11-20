def remove_runs(ns):
    new_list = []

    if len(ns) == 1:
        new_list = ns
    elif len(ns) > 1:
        for item in ns:
            if len(new_list) == 0 or item != new_list[len(new_list)-1]:
                new_list.append(item)
    
    return new_list