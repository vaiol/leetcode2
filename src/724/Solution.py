from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            total_sum += n
        left_sum = 0
        for i, n in enumerate(nums):
            if total_sum - left_sum - n == left_sum:
                return i
            left_sum += n
        return -1


