from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        hMax = max(b - a for a,b in zip(horizontalCuts, horizontalCuts[1:]))
        wMax = max(b - a for a,b in zip(verticalCuts, verticalCuts[1:]))
        return (hMax * wMax) % (10**9 + 7)
