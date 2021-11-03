# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total_sum = 0

        stack = deque()
        stack.append((root, 0))
        while stack:
            node, curr_sum = stack.pop()
            curr_sum = curr_sum * 10 + int(node.val)

            if not node.left and not node.right:
                total_sum += curr_sum
                
            if node.right:
                stack.append((node.right, curr_sum))
            if node.left:
                stack.append((node.left, curr_sum))
        return total_sum

    def sumNumbersRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_sum = 0
        
        def dfs(node: TreeNode, curr_sum: int):
            nonlocal total_sum
            curr_sum = curr_sum * 10 + int(node.val)
            if not node.right and not node.left:
                total_sum += curr_sum
                return
            
            if node.left:
                dfs(node.left, curr_sum)
            
            if node.right:
                dfs(node.right, curr_sum)
        
        dfs(root, 0)
        
        return total_sum