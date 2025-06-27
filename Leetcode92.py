# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left ==right:
            return head
        counter = 1
        current = head
        prev = None
        left_prev = None

        while True:

            if counter < left:
                print(1)
                prev = current
                current = current.next

            elif counter == left:
                print(2)
                left_prev = prev

                prev = current

                current = current.next
            elif counter > left and counter < right:
                print(3)
                next = current.next
                current.next = prev
                prev = current
                current = next
            if counter == right:
                print(4)
                print(prev)
                next = current.next
                current.next = prev
                if left_prev.next.next:
                    left_prev.next.next = next
                left_prev.next = current
                break
            counter+=1

        return head

l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2,l3)
l1 = ListNode(1, l2)
s = Solution()
res = s.reverseBetween(l1, 2,4)
print(res)







