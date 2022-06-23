def length_calculation(my_val):
    len_val = 0
    while(my_val != 0):
        len_val = len_val + 1
        my_val = my_val//10
    return len_val
def digit_sum(my_num):
    remaining = sum_val = 0
    len_fun = length_calculation(my_num)
    while(my_num > 0):
        remaining = my_num%10
        sum_val = sum_val + (remaining**len_fun)
        my_num = my_num//10
        len_fun = len_fun - 1
    return sum_val
ini_result = 0
print("The disarium numbers between 1 and 100 are : ")
for i in range(1, 101):
    ini_result = digit_sum(i)
    if(ini_result == i):
        print(i)