# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        items = [None, None]
        stack = [[root, 0, None]]
        while stack:
            el, level, parent = stack.pop(0)
            if el.val == x:
                items[0] = [level, parent]
            if el.val == y:
                items[1] = [level, parent]
            if items[0] and items[1]:
                break

            if el.left:
                stack.append([el.left, level + 1, el.val])
            if el.right:
                stack.append([el.right, level + 1, el.val])
        if items[0] and items[1] and items[0][0] == items[1][0] and items[0][1] != items[1][1]:
            return True
        return False
