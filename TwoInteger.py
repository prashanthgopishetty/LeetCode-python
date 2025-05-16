class Solution:
    def twoSum(self, nums, target):
        s = {}
        for idx, i in nums:
            if target-i in s:
                return [idx, s[target-i]]
            s[i] = idx

s = Solution()
print(s.twoSum([3,4,5,6],7))