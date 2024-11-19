# write your code here
def domino_chain(dominos):
    if len(dominos) < 2:
        return True
    for i in range(len(dominos)-1):
        card_1 = dominos[i]
        card_2 = dominos[i+1]
        if card_1[1] != card_2[0]:
            return False
    return True
