from collections import deque
from typing import List

class Solution:
    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1

s = Solution()
nums = [0,0,1,1,1,0,0]
res = s.longestOnes(nums, 2)
print(res)