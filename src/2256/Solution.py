class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        temp_sum = 0
        prefix_sum = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            prefix_sum[i] = temp_sum
            temp_sum += nums[i]
        
        temp_sum = 0
        min_avarage = float('inf')
        ans = len(nums) - 1
        for i in range(len(nums)):
            temp_sum += nums[i]
            left_avarage = temp_sum // (i + 1)
            right_count = (len(nums) - (i + 1))
            right_avarage = 0 if right_count == 0 else prefix_sum[i] // right_count
            avarage = abs(left_avarage - right_avarage)
            if avarage < min_avarage:
                ans = i
                min_avarage = avarage
                
        return ans
        
        