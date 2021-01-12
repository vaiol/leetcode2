from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = sum(grid, [])
        resArr = [None] * (m * n)
        resArrlen = len(resArr)
        for it, val in enumerate(arr):
            index = (it + k) % resArrlen
            grid[index // n][index % n] = val
        return grid