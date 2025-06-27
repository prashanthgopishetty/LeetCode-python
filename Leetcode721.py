from collections import defaultdict
from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        email_dict = {}
        counter = 0
        for  l in accounts:

            merge_idx = -1
            for idx, email in enumerate(l[1:]):
                if email in email_dict:
                    merge_idx = idx
                    break

            if merge_idx >=0:
                res[merge_idx].extend(l[1:])
                i = merge_idx
                merge_idx = -1
            else:
                res.append(l)
                i = counter
                counter+1
            for email in l[1:]:
                email_dict[email] = i
            print(res)

        return res
accounts =[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
s = Solution()
print(s.accountsMerge(accounts))





