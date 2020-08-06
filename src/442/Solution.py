from collections import Counter
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [n for n in c if c[n] > 1]