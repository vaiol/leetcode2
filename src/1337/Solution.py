from typing import List


class Solution:
    def binarySearch(self, row: List[int]):
        start = 0
        end = len(row) - 1
        while start <= end:
            mid = (end + start) // 2
            if row[mid] == 1:
                start = mid + 1
            else:
                end = mid - 1
        return len(row) - (len(row) - start)

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = [[0] * 2 for _ in range(len(mat))]
        for i, row in enumerate(mat):
            d[i][1] = i
            d[i][0] = self.binarySearch(row)
        s = sorted(d)
        return [n[1] for n in s[:k]]

