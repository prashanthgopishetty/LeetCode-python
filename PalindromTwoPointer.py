class Solution:
    def isPalindrome(self, s):
        start = 0
        end = len(s)-1
        res = False
        while start < end:
            if not s[start].isalnum():
                start+=1
                continue
            elif not s[end].isalnum():
                end-=1
                continue
            if(s[start].lower() != s[end].lower()):
                break
            else:
                start+=1
                end-=1
        else:
            res = True
        return res
s= Solution()
s1="Was it a car or a cat I saw?"
print(s.isPalindrome(s1))
