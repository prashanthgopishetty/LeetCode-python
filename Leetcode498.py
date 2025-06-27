from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        M = len(mat)
        N = len(mat[0])

        up = True
        i, j  = 0, 0
        res = [mat[i][j]]
        while True:
            if up:
                if i==0 and j==N-1:
                    i = i+1
                    up = False
                elif i==0:
                    j= j+1
                    up = False
                elif j==N-1:
                    i = i+1
                    up = False
                else:
                    i= i-1
                    j= j+1

            else:
                if i == M-1 and j==0:
                    j = j+1
                    up = True
                elif j==0:
                    i = i+1
                    up = True
                elif i == M-1:
                    j = j+1
                    up = True
                else:
                    i = i+1
                    j = j-1

            res.append(mat[i][j])
            if i == M-1 and j == N-1:
                break
        return res

s = Solution()
mat =[[2,5],[8,4],[0,-1]]
print(s.findDiagonalOrder(mat))



