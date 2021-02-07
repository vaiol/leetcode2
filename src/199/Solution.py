# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = []
    def rightSide(self, root: TreeNode, level: int) -> None:
        if not root:
            return
        if level > len(self.out):
            self.out.append(root.val)
        self.rightSide(root.right, level + 1)
        self.rightSide(root.left, level + 1)
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.rightSide(root, 1)
        return self.out