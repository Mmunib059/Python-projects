# Write a recursive function to calculate the sum of first n natural numbers.

def cal_sum(a):
    if a == 0:
        return 0 
    # print(a)
    return cal_sum(a-1) + a

sum = cal_sum(7)
print(sum)