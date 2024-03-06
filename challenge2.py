def returns_max_sum(all_ints):
    max_sum2=[]    
    for a in range(0,len(all_ints)-1):
        #print(str(all_ints[a]))
        my_num1=sum(int(all_num) for all_num in str( all_ints[a]))
        my_num2=sum(int(all_num) for all_num in str(all_ints[a+1]))
        if my_num2==my_num1:
           # print(my_num1)
            total_nums=all_ints[a]+all_ints[a+1]
           # print(total_nums)
            max_sum2.append(total_nums)
    if not  max_sum2:
        return -1
    #print(max_sum2)
    return min(max_sum2)
my_result=returns_max_sum([51, 71, 17, 42])
print(my_result)
      
