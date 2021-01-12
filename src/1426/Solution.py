from collections import Counter
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        c = Counter(arr)
        for value, counter in c.items():
            if c.get(value + 1):
                res += counter
        return res
