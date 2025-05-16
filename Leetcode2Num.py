# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack = []
        mod = 0
        while l1 is not None:
            res = mod+l1.val+l2.val
            if(l1.next is None):
                stack.append(res)
            else:
                stack.append(res%10)
                mod = res//10

            l1 = l1.next
            l2 = l2.next

        return int(''.join(str(num) for num in stack))

l3  = ListNode(3,None)
l2  = ListNode(4,l3)
l1  = ListNode(2,l2)

l6  = ListNode(4,None)
l5  = ListNode(6,l6)
l4  = ListNode(5,l5)
s= Solution()
print(s.addTwoNumbers(l1,l4))