# write your code here
def split_in_two(xs):
    first_half = ()
    second_half = ()

    middle = int(len(xs)/2)
    if len(xs) % 2:
        middle += 1

    first_half = xs[0: middle]
    second_half = xs[middle:]
    return (first_half, second_half)
