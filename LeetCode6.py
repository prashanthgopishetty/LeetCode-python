class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(len(s) <2 or numRows == 1 or numRows >= len(s)):
            return s

        fs = s[::2*(numRows-1)]
        res =[fs]

        for i in range(1, numRows-1):
            steps=[2*(numRows-i+1)-4, 2*(i)]
            temp=s[i]
            toggle = False
            while i< len(s):
                i+=steps[toggle]
                if(i < len(s)):
                    temp+=s[i]
                    toggle = not toggle

            res.append(temp)


        ls = s[numRows-1::2*(numRows-1)]
        res.append(ls)
        return "".join(res)

s= Solution()

print(s.convert("PAYPALISHIRING",3))