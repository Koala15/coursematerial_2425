# write your code here
def increase_version(version, breaking_change, new_features):
    major, minor, patch = version
    if breaking_change:
        major += 1
        minor = 0
        patch = 0
    elif new_features:
        minor += 1
        patch = 0
    else:
        patch += 1
    return (major, minor, patch)


def is_more_recent(v1, v2):
    major1, minor1, patch1 = v1
    major2, minor2, patch2 = v2

    if  major1 > major2:
        return True
    elif major1 == major2:
        if minor1 > minor2:
            return True
        elif minor1 == minor2:
            if patch1 > patch2:
                return True
    return False

"""def is_more_recent(v1, v2):
    return v1 > v2"""

def is_older(v1, v2):
    return v1 < v2