
class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for n in nums:
            d[n] = d.get(n,-1)+1

        nd = dict(sorted(d.items(),key= lambda item:item[1], reverse=True))
        return list(nd.keys())[0:k]
s= Solution()
print(s.topKFrequent([1,2,2,3,3,3],2))