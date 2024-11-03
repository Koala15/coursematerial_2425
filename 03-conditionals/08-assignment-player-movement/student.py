# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    new_position = position
    if left_arrow == True:
        if shift == True:
            new_position =  new_position - 2
        else:
            new_position = new_position - 1

    if right_arrow == True:
        if shift == True:
            new_position =  new_position + 2
        else:
            new_position = new_position + 1
    return new_position