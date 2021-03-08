from functools import lru_cache
from typing import List


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def helper(total: int) -> int:
            if total < 0:
                return float('inf')
            if total == 0:
                return 0
            return min(1 + helper(total - coin) for coin in reversed(coins))
        res = helper(amount)
        return -1 if res == float('inf') else res
    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
    
        return -1 if dp[-1] == float('inf') else dp[-1]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
    
        return -1 if dp[-1] == float('inf') else dp[-1]
