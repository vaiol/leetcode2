# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeRec(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        right = self.invertTreeRec(root.right)
        left = self.invertTreeRec(root.left)
        root.left = right
        root.right = left
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque()
        queue.append(root)
        while queue:
            item = queue.popleft()
            item.left, item.right = item.right, item.left
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        
        return root
        
        # preorder traversal, store values as an array
        # postorder traversal, update value for each node from arry
        
        
        