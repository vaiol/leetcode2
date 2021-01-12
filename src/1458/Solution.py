from functools import lru_cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = nums1, nums2
        @lru_cache(maxsize=None)
        def LCS(i1: int, i2: int):
            if len(n1) == i1 or len(n2) == i2:
                return float('-inf')
            case_1 = LCS(i1 + 1, i2)
            curr_val = n1[i1] * n2[i2]
            case_2 = curr_val + LCS(i1 + 1, i2 + 1)
            case_3 = LCS(i1, i2 + 1)
            return max(case_1, case_2, case_3, curr_val)
        return LCS(0, 0)
