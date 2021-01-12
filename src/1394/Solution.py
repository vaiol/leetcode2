from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        target = -1
        for num, count in counts.items():
            if num == count and target < num:
                target = num
        return target
