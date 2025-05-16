class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        len =0;
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[start])
                start +1
            charSet.add(s[r])
            res = max(len, r-start+1)
        return res

s = Solution()
print(s.lengthOfLongestSubstring("abcdefaefarbc"))