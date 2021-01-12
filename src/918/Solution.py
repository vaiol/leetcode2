from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total_sum = 0
        max_sum, local_max_sum = float("-inf"), 0
        min_sum, local_min_sum = float("inf"), 0
        
        for n in A:
            total_sum += n
            local_max_sum = max(n, local_max_sum + n)
            max_sum = max(max_sum, local_max_sum)
            
            local_min_sum = min(n, local_min_sum + n)
            min_sum = min(min_sum, local_min_sum)
        
        circular_sum = total_sum - min_sum or float("-inf")
        return max(circular_sum, max_sum)
