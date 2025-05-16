class Solution:
    def isPalindrome(self, s):
        l = 0
        r =len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True




s= Solution()
print(s.isPalindrome('abccba'))