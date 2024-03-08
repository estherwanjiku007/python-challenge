#inputs:a list
def sum_max(an_array):
    # checking if possible to have 10 bricks in each box 
    total_bricks2 = sum(an_array)
    no_of_boxes2 = len(an_array)
    if total_bricks2 != 10 * no_of_boxes2:
        return -1 
    # keep track of the moves 
    moves = 0
    # iterate over the boxes 
    for i in range(no_of_boxes2):
        # check each brick for any deficit or excess
        if an_array[i] > 10:
            diff = an_array[i] - 10 
            # if any excess i move the excess to the brick 
            an_array[i] -= diff
            an_array[i + 1] += diff            # update my moves 
            moves += diff
            #  deficit 
        elif an_array[i] < 10:
            diff = 10 - an_array[i]
            # if any deficit , bring in the diff. from the next box 
            an_array[i] += diff
            an_array[i + 1] -=diff
            moves += diff
    return moves 
print(sum_max([7,15,10,8]))