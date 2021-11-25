class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(1, N):
            nums[i] = max(nums[i] + nums[i - 1], nums[i])

        return max(nums)
