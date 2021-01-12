from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        res = 0
        for n in nums:
            res += 1
            if n == 0:
                res = 0
            m = max(res, m)
        return m
