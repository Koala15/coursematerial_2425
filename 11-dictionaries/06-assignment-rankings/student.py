def rankings(participants):
    my_rankings = {}
    rank = 1
    for x in participants:
        my_rankings[x] = rank
        rank +=1
    return my_rankings
