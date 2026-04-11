# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, head

        i = 0
        while n:
            r = r.next
            n -= 1
        
        while 1:
            if not r:
                l.next = l.next.next
                break
            r = r.next
            l = l.next

        
        return dummy.next

