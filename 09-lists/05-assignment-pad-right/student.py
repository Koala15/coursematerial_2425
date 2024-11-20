def pad_right(xs, length, padding):
    for i in range(length - len(xs)):
        xs.append(padding)