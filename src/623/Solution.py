# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v, root)
            return new_root
        def dfs(head: TreeNode, level: int):
            if not head:
                return
            if level + 1 == d:
                left = TreeNode(v, head.left)
                right = TreeNode(v, None, head.right)
                head.left = left
                head.right = right
            else:
                dfs(head.left, level + 1)
                dfs(head.right, level + 1)
        dfs(root, 1)
        return root