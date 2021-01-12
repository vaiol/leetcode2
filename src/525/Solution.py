from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_count = 0
        d = dict()
        count = 0
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                count -= 1
            if count == 0:
                max_count = i + 1
            if count in d:
                max_count = max(i - d.get(count), max_count)
            else:
                d[count] = i
        return max_count
