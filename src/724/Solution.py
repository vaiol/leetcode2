from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = 0
        d = dict()
        for i, n in enumerate(nums):
            d[i] = s
            s += n
        for i in d:
            right_sum = s - nums[i] - d[i]
            if right_sum == d[i]:
                return i
        return -1


