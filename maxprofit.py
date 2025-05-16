from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        start = 0
        end = 0
        for i,v in enumerate(prices):
            end = i
            if maxprofit > (prices[end]-prices[start]):
                start = end

            maxprofit =max(maxprofit, prices[end]-prices[start])
        return maxprofit

s = Solution()
prices=[7,1,5,3,6,4]

print(s.maxProfit(prices))