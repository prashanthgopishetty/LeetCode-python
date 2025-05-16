from typing import  List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for c in tokens:
            if c == "+":
                s.append(s.pop()+s.pop())
            elif c == "-":
                s.append(s.pop()-s.pop())
            elif c == "*":
                s.append(s.pop()*s.pop())
            elif c == "/":
                a, b = s.pop(), s.pop()
                s.append(int(float(b) / a))
            else:
                s.append(int(c))
        return s[0]

tokens = ["1","2","+","3","*","4","-"]
s = Solution()
print(s.evalRPN(tokens))