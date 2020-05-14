from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = dict()
        sorted_nums = sorted(nums)
        for i, n in enumerate(sorted_nums):
            if n not in d:
                d[n] = i
        return [d[n] for n in nums]

