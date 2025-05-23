from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return res
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res



s = Solution()
print(s.generateParenthesis(3))