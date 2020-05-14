from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        counter = Counter(A)
        res = -1
        for num, count in counter.items():
            if count == 1 and num > res:
                res = num
        return res