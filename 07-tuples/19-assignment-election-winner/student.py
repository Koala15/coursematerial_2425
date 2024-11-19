# write your code here
def election_winner(votes):
    if len(votes) == 0:
        return None

    if len(votes) == 1:
        return votes[0]

    sorted_votes = sorted (votes)
    winner_name = sorted_votes[0]
    winner_counts = 1
    current_counts = 1
    current_name = sorted_votes[0]

    for name in sorted_votes[1:]:
        if name == current_name:
            current_counts +=1
        else:
            current_counts = 1 
            current_name = name

        if current_counts > winner_counts:
            winner_counts = current_counts
            winner_name = name

    return winner_name