class Solution:
    def maxProduct_1(self, nums: List[int]) -> int:
        # 03.12.2021 greedy algorithm, two pass approach - from left to right and from right to left
        N = len(nums)
        if N == 1:
            return nums[0]

        normal_strategy_arr = [0] * N
        minus_strategy_arr = [0] * N
        minus_reverse_strategy_arr = [0] * N
        
        
        normal_strategy_arr[0] = max(0, nums[0])
        minus_strategy_arr[0] = nums[0]
        for i in range(1, N):
            current_n = nums[i]
            if current_n == 0:
                continue
            if current_n > 0:
                normal_strategy_arr[i] = max(current_n * normal_strategy_arr[i - 1], current_n)
            minus_strategy_arr[i] = current_n * minus_strategy_arr[i - 1] if minus_strategy_arr[i - 1] != 0 else current_n
            
        minus_reverse_strategy_arr[N - 1] = nums[N - 1]
        for i in range(N-2, -1, -1):
            current_n = nums[i]
            minus_reverse_strategy_arr[i] = current_n * minus_reverse_strategy_arr[i + 1] if minus_reverse_strategy_arr[i + 1] != 0 else current_n
        
        return max(max(normal_strategy_arr), max(minus_strategy_arr), max(minus_reverse_strategy_arr))
    
    def maxProduct(self, nums: List[int]) -> int:
        # 03.12.2021 kedanes algo based on leetcode solution
        max_product = nums[0]
        min_product = nums[0]
        
        result = max_product
        
        for i in range(1, len(nums)):
            n = nums[i]

            current_max = max(n, max_product * n, min_product * n)
            min_product = min(n, max_product * n, min_product * n)
            max_product = current_max
            
            result = max(max_product, result)
        
        return result
            
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
