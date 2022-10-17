# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if not root:
            return []
        self.traversal(root.left, res)
        self.traversal(root.right, res)
        res.append(root.val)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.traversal(root, [])
        if not root:
            return []
        s1 = deque()
        s2 = deque()
        
        s1.append(root)
        while s1:
            item = s1.pop()
            s2.append(item)
            if item.left:
                s1.append(item.left)
            if item.right:
                s1.append(item.right)
        
        res = []
        while s2:
            item = s2.pop()
            res.append(item.val)
        return res
        