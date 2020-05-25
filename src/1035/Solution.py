from functools import lru_cache
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        @lru_cache(maxsize=None)
        def LCS(i1, i2):
            if len(A) == i1 or len(B) == i2:
                return 0
            if A[i1] == B[i2]:
                return 1 + LCS(i1 + 1, i2 + 1)
            return max(LCS(i1 + 1, i2), LCS(i1, i2 + 1))
        return LCS(0, 0)
