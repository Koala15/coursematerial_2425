def counts(xs):
    result = dict()
    for x in xs:
        count = result.get(x,0) + 1
        result[x] = count
    return  result
