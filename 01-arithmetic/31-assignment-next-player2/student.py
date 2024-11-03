# write your code here
import math

def next_player2(player, player_count):
    minimum = min(player + 1, (player % player_count) + 1)
    return minimum