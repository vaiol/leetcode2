from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = float('inf')
        S = 0
        left, right = 0, 0
        while right < len(nums):
            S += nums[right]
            while S >= s:
                ans = min(ans, right - left + 1)
                S -= nums[left]
                left += 1
            right += 1
        return ans if ans != float("inf") else 0
