def sum_max(an_array):      
     total_moves=0  
     my_total=sum(an_array)
     if my_total%10==0:
         for a in range(0,len(an_array)):
             if an_array[a]>10:
                 the_diff=an_array[a]-10
                 an_array[a]-=the_diff
                 total_moves+=the_diff
                 total_moves=all_list(an_array,total_moves,the_diff)
     else:return -1
              
    # print(an_array)
     return total_moves

def all_list(an_array,total_moves,the_diff):
    for b in range(0,len(an_array)):
        if an_array[b]<10:
            the_diff2=10-an_array[b]
            if the_diff2<=the_diff:
             an_array[b]+=the_diff2
             total_moves+=the_diff2-1
            else:
                an_array[b]+=the_diff
                total_moves+=1     

            return total_moves

result =sum_max([11, 10, 8, 12, 8, 10, 11])
print(result)