# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        found = None

        def dfs(node: TreeNode, prev_count = 0):
            nonlocal found
            if not node:
                return prev_count
            count = 1
            count += dfs(node.left, prev_count)
            if count == k:
                found = node.val
            return dfs(node.right, count)

        dfs(root)
        return found
