from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums :
            idx = abs(num) - 1
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1
        return -1

s = Solution()
res = s.findDuplicate([3,4,2,1,4,4])
print(res)