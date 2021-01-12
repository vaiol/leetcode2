# Definition for a binary tree node.
from collections import Counter
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:

        def checkPseudoPalindrome(path: List[int]) -> bool:
            r = False
            c = Counter(path)
            for n,v in c.items():
                if v % 2 != 0:
                    if r is True:
                        return False
                    r = True
            return True

        def dfs(node: TreeNode, path: List[int]) -> int:
            if not node:
                return 0
            current_path = path + [node.val]
            if not node.left and not node.right:
                if checkPseudoPalindrome(current_path):
                    return 1
                else:
                    return 0
            return dfs(node.left, current_path) + dfs(node.right, current_path)
        return dfs(root, [])
