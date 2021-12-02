from functools import lru_cache
from typing import List


class Solution:
    def robRec(self, nums: List[int]) -> int:
            N = len(nums) - 1

            @lru_cache()
            def rec(index: int):
                nonlocal nums
                if index <= 1:
                    return nums[index]
                if index == 2:
                    return nums[index] + rec(index - 2)
                return nums[index] + max(rec(index - 2), rec(index - 3))

            return max(rec(N), rec(N - 1))

    def rob(self, nums: List[int]) -> int:
        M = len(nums)
        
        res = [0] * M
        
        for i in range(M):
            if i <= 1:
                res[i] = nums[i]
            elif i == 2:
                res[i] = nums[i] + res[i - 2]
            else:
                res[i] = nums[i] + max(res[i - 2], res[i - 3])
        return max(res[M - 1], res[M - 2])
