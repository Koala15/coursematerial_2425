# write your code here
def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 0
    elif player1_choice > player2_choice:
        if player2_choice == 0 and player1_choice ==2:
            return 2
        return 1
    elif player1_choice < player2_choice:
        if player1_choice ==0 and player2_choice == 2:
            return 1
        return 2
    