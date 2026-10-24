class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Solution:
    def middleNode(self, head):
        # Handle the edge case of an empty list
        if not head:
            return None
            
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
