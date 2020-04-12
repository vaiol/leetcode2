from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        computed_sum = [0] * len(nums)
        for i, n in enumerate(nums):
            computed_sum[i] = total_sum
            total_sum += n
        for i in range(len(nums)):
            right_sum = total_sum - nums[i] - computed_sum[i]
            if right_sum == computed_sum[i]:
                return i
        return -1


