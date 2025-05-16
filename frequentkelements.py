class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = 1+ count.get(n,0)

        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for p in freq[i]:
                res.append(p)
                if(len(res)==k):
                    return res
s = Solution()
print(s.topKFrequent([1,2,2,3,3,3], 2))
