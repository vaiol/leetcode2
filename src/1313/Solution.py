from typing import List


class Solution:
    def generateArray(self, freq, val):
        return [val] * freq

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            res += self.generateArray(nums[i], nums[i + 1])
        return res
