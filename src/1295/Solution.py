from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                c += 1
        return c