# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        l,r  = head,head

        while r and r.next:
            if l == r.next:
                return True
            else:
                r = r.next.next
                l = l.next
        return False
        