# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Below uses extra space
        # nodes = set()
        # while head:
        #     if head not in nodes:
        #         nodes.add(head)
        #         head = head.next
        #     else:
        #         return True
        # return False

        # without extra space
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False