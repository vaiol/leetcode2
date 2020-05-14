from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        mid = n // 2
        i, j = 0, n - 1
        while i < j:
            res[i] = -mid
            res[j] = mid
            mid -= 1
            i += 1
            j -= 1
        return res
