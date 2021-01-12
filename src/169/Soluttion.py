from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        c = Counter(nums)
        for num in c:
            if c[num] > target:
                return num
        return -1
