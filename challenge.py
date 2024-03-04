def sum_max(an_array):      
    total_moves=0   
    for i in range(0,len(an_array)):        
            
        if an_array[i]>10:
           new_array2= an_array[i]-10
           total_moves=total_moves+new_array2
          # print(f" total moves {total_moves}")
           #return total_moves
          # print(total_moves)
        elif an_array[i]<10:
            my_count2=10-an_array[i]
            total_moves=total_moves-my_count2
            print(f"total moves  {my_count2}")
          #  print(f"total_moves {total_moves}")
            #return total_moves
        elif an_array[i]==an_array[i]:
            total_moves=total_moves+0
           # print(f"total moves {total_moves}")
           # return -1
        #else:print(-1)
            #print(total_moves)
    #print(total_moves)
    print(total_moves)       
    return total_moves        
    
result =sum_max([15,10,8,7])
#print(result)
max_sum2=[]
def returns_max_sum(all_ints):    
    for a in range(0,len(all_ints)-1):
        my_num1=sum(int(all_num) for all_num in str( all_ints[a]))
        my_num2=sum(int(all_num) for all_num in str(all_ints[a+1]))
        if my_num2==my_num1:
            total_nums=all_ints[a]+all_ints[a+1]
            max_sum2.append(total_nums)
    if not  max_sum2:
        return -1
    return max(max_sum2)
my_result=returns_max_sum([15, 19, 82, 46, 47])
print(my_result)
      
       
result=returns_max_sum([51, 71, 17, 42])

the_list2=list()
all_list2=["Esther","Beatrice","BEN","Wanjiku","Mugo"] 
def gives_string(an_int,all_list):  
   new_list=list()  
   for a in all_list:
             
         if len(a)==an_int :
          new_list.append(a.lower())     
          
         else:print(-1)
          
   return new_list
result=gives_string(3,all_list2)
print(result)

        
