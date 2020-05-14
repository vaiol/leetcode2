from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for a, b in zip(points[0:], points[1:]):
            res += max(abs(a[0] - b[0]), abs(a[1] - b[1]))
        return res


