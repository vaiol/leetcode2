# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricRL(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not l and not r:
            return True
        if not l or not r or l.val != r.val:
            return False
        return self.isSymmetricRL(l.right, r.left) and self.isSymmetricRL(l.left, r.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricRL(root.left, root.right)
        