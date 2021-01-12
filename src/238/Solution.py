from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        summ = 1
        for i, n in enumerate(nums):
            result[i] = summ
            summ *= n

        summ = 1
        for i, n in enumerate(reversed(nums)):
            result[length - i - 1] = result[length - i - 1] * summ
            summ *= n
        return result