from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        mi, ni = 0, 0
        mii, nii = len(matrix) - 1, len(matrix[0]) - 1

        res = []
        con = True
        while con:
            con = False
            if mi <= mii:
                for i in range(ni, nii + 1):
                    res.append(matrix[mi][i])
                mi += 1
                con = True
            if ni <= nii:
                for i in range(mi, mii + 1):
                    res.append(matrix[i][nii])
                nii -= 1
                con = True
            if mi <= mii:
                for i in reversed(range(ni, nii + 1)):
                    res.append(matrix[mii][i])
                mii -= 1
                con = True
            if ni <= nii:
                for i in reversed(range(mi, mii + 1)):
                    res.append(matrix[i][ni])
                ni += 1
                con = True

        return res
