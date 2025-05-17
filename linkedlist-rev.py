def solution(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

n1 = Node(5,None)
n2 = Node(4, n1)
n3 = Node(3, n2)
n4 = Node(2, n3)
n5 = Node(1, n4)
res = solution(n5)
print(res)
