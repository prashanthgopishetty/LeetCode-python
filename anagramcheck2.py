from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
print(is_anagram('taste is mine', 'state'))
print(is_anagram('beach', 'peach'))