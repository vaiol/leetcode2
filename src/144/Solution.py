# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_traversal_rec(self, curr: Optional[TreeNode], res=[]) -> List[int]:
        if not curr:
            return
        res.append(curr.val)
        self.preorder_traversal_rec(curr.left, res)
        self.preorder_traversal_rec(curr.right, res)
        return res
    
    def preorder_traversal(self, curr: Optional[TreeNode]) -> List[int]:
        if not curr:
            return []
        res = []
        stack = []
        stack.append(curr)
        while stack:
            item = stack.pop()
            if item:
                res.append(item.val)
                stack.append(item.right)
                stack.append(item.left)
        
                
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.preorder_traversal(root)
        
        