class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0 for _ in range(amount)]
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]
        return dp[-1]