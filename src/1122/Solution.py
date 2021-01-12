from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = [0] * len(arr1)
        counter = Counter(arr1)
        i = 0
        for n in arr2:
            j = 0
            maxEl = counter.get(n)
            while j < maxEl:
                res[i + j] = n
                j += 1
            i += j
            del counter[n]
        for n in sorted(counter):
            j = 0
            maxEl = counter.get(n)
            while j < maxEl:
                res[i + j] = n
                j += 1
            i += j
        return res
