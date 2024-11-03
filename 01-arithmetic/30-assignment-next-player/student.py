# write your code here
import math

def next_player(player, player_count):
    minimum = min(player + 1, (player + 1) % player_count)
    return minimum