from typing import List

# 1441
# 5404. Build an Array With Stack Operations

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        j = 0
        for i in range(1, n + 1):
            if j >= len(target):
                return res
            res.append("Push")
            if i == target[j]:
                j += 1
            else:
                res.append("Pop")
        return res
