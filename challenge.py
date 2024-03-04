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
              
     print(an_array)
     return total_moves

def all_list(an_array,total_moves,the_diff):
    for b in range(0,len(an_array)):
        if an_array[b]<10:
            the_diff2=10-an_array[b]
            if the_diff2<=the_diff:
             an_array[b]+=the_diff2
             total_moves+=1
            else:
                an_array[b]+=the_diff
                total_moves+=1     

            return total_moves

result =sum_max([11,10,9])
print(result)
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
my_result=returns_max_sum([51, 71, 17, 42])
print(my_result)
      
       
result=returns_max_sum([51, 71, 17, 42])

the_list2=list()
all_list2=["Esther","Beatrice","BEN","Wanjiku","Mugo"] 
def gives_string(an_int,all_list):  
   new_list=list()  
   for a in all_list:
             
         if len(a)==an_int :
          new_list.append(a.lower())     
          
         else:continue
          
   return new_list
result=gives_string(3,all_list2)
print(result)

        
