# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            additional_aueue = deque()
            level = []
            while queue:
                item = queue.popleft()
                level.append(item.val)
                if item.left:
                    additional_aueue.append(item.left)
                if item.right:
                    additional_aueue.append(item.right)
            queue.extend(additional_aueue)
            res.append(level)
        return res
                
        