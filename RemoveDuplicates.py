class Solution:
    def hasDuplicate(self, nums):
        m = set()
        for n in nums:
            if(n in m):
                return False
            m.add(n)
        else:
            return True
s= Solution()
print(s.hasDuplicate([1,2,3,3]))