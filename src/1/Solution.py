from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            if d.get(target - n) != None:
                return [d.get(target - n), i]
            else:
                d[n] = i
