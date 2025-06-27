from typing import List
class Solution:
    def move_zero(self, a : List):
        size = 0

        for i in range(len(a)):
            if a[i]==0:
                size+=1
            else:
                a[i-size],a[i] =a[i], a[i-size]
        return a

s =Solution()
r = s.move_zero([1,0,1,2,0,4,5,6])
print(r)
