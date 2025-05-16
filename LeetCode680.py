class Solution:
    def isPalindrome(self,s):
        l = 0
        r = len(s)-1
        while (l < r):
            if(s[l]!=s[r]):
                return self.isValidPalindrome(s[l+1:r+1]) or self.isValidPalindrome(s[l:r])
            l+=1
            r-=1

        return True

    def isValidPalindrome(self, s):
        l = 0
        r = len(s)-1
        while(l < r):
            if(s[l] != s[r]):
                return False
        return True




s = Solution()
print(s.isPalindrome("deeee"))
