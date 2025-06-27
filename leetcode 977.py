from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        if nums[0] >=0 or len(nums)<2:
            return [x**2 for x in nums]
        elif nums[-1]<=0:
            return [x**2 for x in nums[::-1]]
        else:

            a, l ,h = nums, 0, len(nums)-1
            mid = 0
            while l<=h:
                mid = (l+h)//2
                if l == h:
                    break
                if a[mid]==0:
                    break
                elif a[mid]>0 and a[mid-1]<0:
                    break
                elif a[mid]>0:
                    h = mid-1
                else:
                    l = mid+1
            idx = mid
            print(idx)
            i = idx
            j = idx-1
            while i< len(nums) and j>=0:
                if abs(nums[j]) < nums[i]:
                    res.append(nums[j]**2)
                    j-=1
                else:
                    res.append(nums[i]**2)
                    i+=1
            if i == len(nums):
                res.extend([x**2 for x in nums[:j+1][::-1]])
            else:
                res.extend([x**2 for x in nums[i:]])
            return res


s = Solution()
nums = [-3,-3,-2,1]


print(s.sortedSquares(nums))



