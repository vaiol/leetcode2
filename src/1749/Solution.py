class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        curr_sum = min_sum = nums[0]
        for i in range(1, n):
            curr_sum = min(nums[i], curr_sum + nums[i])
            min_sum = min(min_sum, curr_sum)
        return max(abs(max_sum), abs(min_sum))