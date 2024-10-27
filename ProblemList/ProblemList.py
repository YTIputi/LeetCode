from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getVal(self):
        return self.val
    
    def getNext(self):
        return self.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3, lastl = ListNode(), None

        node1, node2 = l1, l2
        sumVal = node1.val + node2.val
        val3 = sumVal % 10
        l3.val = val3
        delta = sumVal - val3

        node1, node2 = l1.next, l2.next
        while node1 or node2:
            ln = ListNode()

            sumVal = node1.val + node2.val
            val3 = sumVal % 10
            ln.val, = val3 + delta

            delta = sumVal - val3




l = ListNode(0)
for i in range(1, 10):
    ld = ListNode(i)
    l.next = ld
    l = ld


node = l
while node:
    print(node.val)
    node = l.next

