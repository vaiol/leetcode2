# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maximum: int):
            if not node:
                return 0
            count = 0
            if node.val >= maximum:
                count += 1
                maximum = node.val
            return count + dfs(node.left, maximum) + dfs(node.right, maximum)
        return dfs(root, float("-inf"))
