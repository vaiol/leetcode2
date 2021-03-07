# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            curr_root, level = queue.popleft()
            if len(levels) < level + 1:
                levels.append([curr_root.val, 1])
            else:
                levels[level][0] += curr_root.val
                levels[level][1] += 1
            if curr_root.left:
                queue.append((curr_root.left, level + 1))
            if curr_root.right:
                queue.append((curr_root.right, level + 1))
        return map(lambda item: item[0] / item[1], levels)