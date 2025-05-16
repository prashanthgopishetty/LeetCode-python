class Solution:
    def isPalindrome(self, x: int) -> bool:
        numstr = str(x)
        l= 0
        r = len(numstr)
        while(l < r):
            if(numstr[l]!= numstr[r]):
                return False
        return True
