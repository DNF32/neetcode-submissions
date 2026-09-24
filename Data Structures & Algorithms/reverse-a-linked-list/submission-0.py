# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n0 = head
        if not n0 or not n0.next:
            return n0
        n1 = head.next
        n0.next = None
            
        while n1:
            n2 = n1.next
            n1.next = n0 
            n0 = n1
            n1 = n2
        return n0

        