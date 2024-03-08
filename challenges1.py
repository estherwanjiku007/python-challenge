# def returns_max_sum(a_list):
#     return sum(int(my_digit) for my_digit in str(a_list))

# print(returns_max_sum([51, 71, 17, 42]))
def my_digit_sum(a_num):
    return sum(int(a_digit) for a_digit in str(a_num))
def returns_max_sum(a_list):
    #max_sum reference
    max_sum=-1
    #ref of the sum results of the digits
    digit_sum={}
    for my_num in a_list:
        sum_digits=my_digit_sum(my_num)
        if sum_digits in digit_sum:
            current_sum=my_num+digit_sum[sum_digits]
            max_sum=max(max_sum,current_sum)
        else:digit_sum[sum_digits]=my_num

    return max_sum
print(returns_max_sum([51, 71, 17, 42]))


