class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        target = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != target[i]:
                res += 1
        return res
