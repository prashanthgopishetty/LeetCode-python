
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2) :
        n = None

        while list1 or list2:
            if list1.val <= list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next

            if not n:
                n = node
                res = node
            else:
                n.next = node
        return res

def list_to_ll(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for i in lst[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

list1=[1,2,4]
list2=[1,3,5]

s = Solution()
res = s.mergeTwoLists(list_to_ll(list1), list_to_ll(list2))
print(res)


