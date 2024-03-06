def sum_max(num_list):
    moves=0
    total_bricks=sum(num_list)
    no_boxes=len(num_list)
    if total_bricks!=10*no_boxes:
        return -1
    #iterate
    for a in range(no_boxes):
        if num_list[a]>10:
            excess=num_list[a]-10            
            num_list[a]-=excess
            num_list[a+1]+=excess            
            moves+=excess
           # print(excess)
        elif num_list[a]<10:
            deficit=10-num_list[a]
            num_list[a]+=deficit
            moves+=deficit
          #  print(moves)
    return moves
print(sum_max([7,15,10,8]))