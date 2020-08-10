# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, target: float) -> int:
        if not node:
            return float('inf')

        cur_diff = abs(node.val - target)
        if node.val > target:
            other_val = self.dfs(node.left, target)
        else:
            other_val = self.dfs(node.right, target)
        other_diff = abs(other_val - target)
        return node.val if other_diff > cur_diff else other_val 
            
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.dfs(root, target)
        