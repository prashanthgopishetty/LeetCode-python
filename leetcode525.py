
def findMaxLength(nums):

    sum = 0
    max_zero_len = -1
    dict_val = {}
    for idx, i in enumerate(nums):
        sum = sum+1 if i ==1 else sum-1
        if sum not in dict_val:
            dict_val[sum] = idx

        if (sum == 0):
            max_zero_len = idx+1
        elif -sum in dict_val:
            max_zero_len = max(max_zero_len, idx-dict_val[-sum])
    return max_zero_len

print(findMaxLength([0,0,1,0,0,0,1,1]))