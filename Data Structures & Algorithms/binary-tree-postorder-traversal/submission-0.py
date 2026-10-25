# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postOrder(root, result)
        return result
        
    def postOrder(self, root, result):
        if not root:
            return
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.val)