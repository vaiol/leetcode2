from typing import List


class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        m = min(A)
        res = 0
        while m > 0:
            res += m % 10
            m = m // 10
        return 0 if res % 2 == 1 else 1
