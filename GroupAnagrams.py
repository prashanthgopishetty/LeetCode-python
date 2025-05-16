from collections import  defaultdict
class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            tmp = [0]*26
            for c in s:
                tmp[ord(c)-ord("a")] += 1
            ans[tuple(tmp)].append(s)
        return ans.values()

s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))