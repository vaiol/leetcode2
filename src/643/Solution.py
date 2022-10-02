class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0
        if len(nums) == k:
            return sum(nums) / k
        
        curr_sum  = sum(nums[0:k])
        max_sum = curr_sum
        left, right = 0, k
        while right < len(nums):
            curr_sum += nums[right]
            curr_sum -= nums[left]
            max_sum = max(max_sum, curr_sum)
            right += 1
            left += 1
            
        # [0, 1, 2, 3, 4]
        return max_sum / k
            
            
            
        
        