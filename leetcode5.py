class Solution(object):
    def longestPalindrome(self, s):
        lps = s[0] if len(s) > 0 else ""
        for i in range(1, len(s)-1):
            #consider odd
            low = i
            high = i
            while(s[low] == s[high]):
                if (len(lps) <  high-low+1):
                    lps = s[low: high+1]
                low-=1
                high+=1
                if(low == -1 or high ==len(s)):
                    break



                    #consider even
            low = i-1
            high = i
            while(s[low] == s[high]):
                if (len(lps) <  high-low+1):
                    lps = s[low: high+1]
                low-=1
                high+=1
                if(low == -1 or high ==len(s)):
                    break




        return lps

s= Solution()
print(s.longestPalindrome("bb"))