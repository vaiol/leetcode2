# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], res: List[int]) -> None:
        if not root:
            return
        self.inorderTraversal(root.left, res)
        res.append(root.val)
        self.inorderTraversal(root.right, res)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_array = []
        self.inorderTraversal(root, sorted_array)
        
        left, right = 0, len(sorted_array) - 1
        while left < right:
            val = sorted_array[left] + sorted_array[right]
            if val == k:
                return True
            if val > k:
                right -= 1
            else:
                left += 1
        return False
        
            
            
        
        
        
        