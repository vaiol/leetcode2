from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        d = defaultdict(list)
        for i in range(M):
            for j in range(N):
                d[i + j].append(matrix[i][j])
        res = []
        reverse = True
        for i in d:
            if reverse:
                res.extend(list(reversed(d[i])))
                reverse = False
            else:
                res.extend(d[i])
                reverse = True
        return res

