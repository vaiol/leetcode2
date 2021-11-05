# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        if not root or (not root.left and not root.right):
            return 0
        queue = deque()
        queue.append((root, False))
        while queue:
            node, is_left = queue.popleft()
            if not node.right and not node.left and is_left:
                total_sum += node.val
                continue
            if node.left:
                queue.append((node.left, True))
            if node.right:
                queue.append((node.right, False))
            
        return total_sum