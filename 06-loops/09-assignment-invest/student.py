def invest(amount, rate, goal):
    count = 0

    while amount < goal:
        count += 1
        amount += amount * rate / 100
        
    return count
