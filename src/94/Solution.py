# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if not root:
            return res
        self.traversal(root.left, res)
        res.append(root.val)
        self.traversal(root.right, res)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.traversal(root, [])
        if not root:
            return []
        res = []
        stack = deque()
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res
            
        