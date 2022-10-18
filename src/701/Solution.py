# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while curr:
            prev = curr
            curr = curr.right if curr.val < val else curr.left
        newNode = TreeNode(val)
        if prev.val > val:
            prev.left = newNode
        else:
            prev.right = newNode
        return root
            
        