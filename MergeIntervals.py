from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        merge_arrays = []
        for i in range(len(intervals)-1):
            if i == len(intervals):
                pass
            else:
                if intervals[i][1]>=intervals[i+1][0]:
                    merge_arrays.append(i)
        new_array = []
        i=0
        while i in range(len(intervals)):
            if i not in merge_arrays:
                new_array.append(intervals[i])
            else:
                start = i
                while i+1 in merge_arrays:
                    i = i+1
                i = i+1
                end = i
                new_array.append([intervals[start][0],intervals[end][1]])
            i = i+1

        return new_array


s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
res = s.merge(intervals)
print(res)