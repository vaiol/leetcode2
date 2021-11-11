class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_v = float('inf')
        step_by_step_sum = 0
        for n in nums:
            step_by_step_sum += n
            min_v = min(min_v, step_by_step_sum)
        return 1 if min_v > 0 else abs(min_v) + 1
        