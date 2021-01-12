from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ri = [0] * n
        ci = [0] * m
        for t in indices:
            ri[t[0]] += 1
            ci[t[1]] += 1
        res = 0
        matrix = [[0] * m] * n
        for i in range(n):
            for j in range(m):
                tmp = ri[i] + ci[j]
                matrix[i][j] += tmp
                if tmp % 2 == 1:
                    res += 1
        return res
