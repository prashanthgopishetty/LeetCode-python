def sliding_window(str):
    left = max_len = 0
    char_set = set()

    for right in range(len(str)):
        while(str[right] in char_set):
            char_set.remove(str[left])
            left+=1
        char_set.add(str[right])
        max_len = max(max_len, right-left+1)
    return max_len

print(sliding_window('abcabcabaccc'))

