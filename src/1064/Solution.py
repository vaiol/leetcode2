from typing import List


class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1
        res = -1
        while (start <= end):
            mid = (start + end) // 2
            if (A[mid] < mid):
                start = mid + 1
            elif (A[mid] > mid):
                end = mid - 1
            else:
                res = mid
                end = mid - 1
        return res
