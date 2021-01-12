from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        D = dict()
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                item = D.get(j - i)
                if (item == None):
                    D[j - i] = n
                elif (item != n):
                    return False
        return True

