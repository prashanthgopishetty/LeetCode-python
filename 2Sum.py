class Solution:
    def twoSum(self, nums, target: int):
        numsMap = {}
        n = len(nums)
        for i in range(n):
            numsMap[nums[i]]=i

        for i in range(n):
            complement = target-nums[i]
            if complement in numsMap and numsMap[complement]!=i:
                return [i, nums[complement]]

s = Solution()
print(s.twoSum([2,7,11,15],9))