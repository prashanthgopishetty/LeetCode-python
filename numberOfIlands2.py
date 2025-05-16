from typing import List
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        visit =set()
        dq = collections.deque()
        neighbors = [[-1,0],[0,-1], [1,0], [0,1]]
        res =0
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]=='1' and (i,j) not in visit:
                    dq.append((i,j))


                    while dq:
                        row,column = dq.popleft()
                        visit.add((i,j))
                        for dr,dc in neighbors:
                            r,c = row+dr, column+dc
                            if min(r,c)< 0 or r >= ROWS or c >= COLUMNS or \
                                    grid[r][c]=='0' or (r,c) in visit:
                                continue
                            dq.append((r,c))
                            visit.add((r,c))
                    res+=1

        return res

grid=[["1","1","0","0","1"],["1","1","0","0","1"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
print(s.numIslands(grid))

