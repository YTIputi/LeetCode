from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        last = 0
        while l1 and l2:   
            newVal = l2.val + l1.val + last
            l2.val = (newVal) % 10
            last = newVal // 10
            current.next = l2
            l2 = l2.next
            l1 = l1.next
            current = current.next
        if last:
            current.next = ListNode(last)
        if l2:
            while l2:            
                newVal = l2.val + last
                l2.val = (newVal) % 10
                last = newVal // 10
                current.next = l2
                l2 = l2.next
                current = current.next
            if last:
                current.next = ListNode(last)
        if l1:
            while l1:
                newVal = l1.val + last
                l1.val = (newVal) % 10
                last = newVal // 10
                current.next = l1
                l1 = l1.next
                current = current.next
            if last:
                current.next = ListNode(last)
        return dummy.next



s = Solution()
# list1 = ListNode(9)
# list1.next = ListNode(9)
# list1.next.next = ListNode(9)
# list1.next.next.next = ListNode(9)
# list1.next.next.next.next = ListNode(9)
# list1.next.next.next.next.next = ListNode(9)
# list1.next.next.next.next.next.next = ListNode(9)


# list2 = ListNode(9)
# list2.next = ListNode(9)
# list2.next.next = ListNode(9)
# list2.next.next.next = ListNode(9)


list1 = ListNode(5)

list2 = ListNode(5)

a = s.addTwoNumbers(list1, list2)
while a:
    print(a.val)
    a = a.next
