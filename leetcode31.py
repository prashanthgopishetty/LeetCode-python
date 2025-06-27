from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                break
        else:
            nums[::-1]



s = Solution()
nums = [1,2,3]
s.nextPermutation(nums)
print(nums)