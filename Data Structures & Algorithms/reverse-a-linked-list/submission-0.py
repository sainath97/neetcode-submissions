# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        prev = None
        later = curr.next
        while curr is not None and curr.next is not None:
            curr.next = prev
            prev = curr
            curr = later
            if curr is not None:
                later = curr.next
        curr.next = prev
        return curr