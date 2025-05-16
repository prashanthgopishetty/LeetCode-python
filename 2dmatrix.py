from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        row = 0
        while top <=bottom:
            row = top+ ((bottom-top)//2)
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break

        left, right = 0, len(matrix[0])-1
        mid = 0
        while left <=right:
            mid= left+ ((right-left)//2)
            if target == matrix[row][mid]:
                return True
            elif target >matrix[row][mid]:
                left = mid+1
            elif target < matrix[row][mid]:
                right = mid-1


        return False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10


s = Solution()
res = s.searchMatrix(matrix, target)
print(res)

