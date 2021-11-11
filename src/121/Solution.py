from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = float('-inf')
        MaxProfit = 0
        for n in reversed(prices):
            Max = max(Max, n)
            MaxProfit = max(MaxProfit, Max - n)
        return MaxProfit

    def maxProfit1(self, prices: List[int]) -> int:
        # 10.11.2021
        if not prices or len(prices) < 2:
            return 0

        max_profit = 0
        stock = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < stock:
                stock = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - stock)
        return max_profit



