def sum_max(an_array):      
    total_moves=0   
    for i in range(0,len(an_array)):        
        #new_array=an_array[i]      
        if an_array[i]>10:
           new_array2= an_array[i]-10
           total_moves=total_moves+new_array2
           return total_moves
          # print(total_moves)
        elif an_array[i]<10:
            my_count2=10-an_array[i]
            total_moves=total_moves-my_count2
            #print(my_count2)
            return total_moves
        elif an_array[i]==an_array[i]:
            total_moves=total_moves
            return -1
            #print(total_moves)
    #print(total_moves)       
    return total_moves        
    
result =sum_max([15,10,8,7])
print(result)
def returns_lower_case(all_ints):
    max_sum1=0
    max_sum2=list()
    count1=0
    count2=0
    for a in all_ints:
        count1=count1+1        
        total=a+(a+1)
        max_sum1=total
        max_sum2.append(max_sum1)
        count2=max(max_sum2)
       # print(max(max_sum2))
   # return max_sum1
       
result=returns_lower_case([3,4,5,6,7])
#print(result)
the_list2=list()
def gives_string(an_int):
   all_list=["Esther","Beatrice","Ben","Wanjiku","Mugo"] 
   new_list=list()  
   for a in all_list:
        if len(a)==an_int:
          new_list.append(a)
          print(a)
          
        else:
           print(-1)
          
   return new_list
result=gives_string(6)
#print(result)

        
