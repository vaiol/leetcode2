# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        return max(self.helper(root.left, depth + 1), self.helper(root.right, depth + 1))
            
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
        