from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_int = [0, -1]
        submax_int = [0, -1]
        for i, n in enumerate(nums):
            if n > max_int[0]:
                submax_int = max_int
                max_int = [n, i]
            elif n > submax_int[0]:
                submax_int = [n, i]
        return max_int[1] if max_int[0] // 2 >= submax_int[0] else -1
