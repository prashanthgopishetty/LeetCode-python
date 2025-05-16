class Solution:
    def isValid(self, s: str) -> bool:
        d = {'}':'{', ')':'(', ']':'['}

        stack = []
        for c in s:
            if c not in d:
                stack.append()
                continue
            if not stack or stack.pop()!= d[c]:
                return False
        return not stack
s= Solution()
print(s.isValid('['))