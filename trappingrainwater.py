from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        storage = 0
        f = 0
        l = len(height)-1
        fmax, lmax = 0,0
        while f <= l:
            if fmax <= lmax:
                f+=1
                if (fmax-height[f] > 0):
                    storage = storage - height[f]+fmax

            else:
                l-=1
                if(lmax-height[l] > 0):
                    storage = storage-height[l]+lmax

        return storage
s = Solution()
res = s.trap([0,2,0,3,1,0,1,3,2,1])
print(res)

