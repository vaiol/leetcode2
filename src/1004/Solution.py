class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        left, right = 0, 0
        
        curr_len = 0
        curr_k = k
        while right < len(nums):
            while right < len(nums) and (nums[right] == 1 or curr_k > 0):
                if nums[right] == 0:
                    curr_k -= 1
                right += 1
            curr_len = right - left
            max_len = max(max_len, curr_len)
            while curr_k == 0 and left < len(nums):
                if (nums[left] == 0):
                    curr_k += 1
                left += 1
        return max_len

    def longestOnes1(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        while right < len(nums):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
            right += 1
        return right - left
            
            
                
