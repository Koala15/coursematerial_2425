def compact(xs):
    ns = []
    for x in xs:
        if not(x is None):
            ns.append(x)
    return ns


def compact_in_place(xs):
    for index in range(len(xs) - 1 , -1, -1):
        if xs[index] is None:
            del xs[index] 
