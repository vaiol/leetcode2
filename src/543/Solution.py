# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.diameter = 0

    def maxLength(self, root: TreeNode) -> int:
        if root:
            left_length = self.maxLength(root.left)
            right_length = self.maxLength(root.right)
            self.diameter = max(left_length + right_length, self.diameter)
            return max(left_length, right_length) + 1
        return 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxLength(root)
        return self.diameter
