from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = float('-inf')
        MaxProfit = 0
        for n in reversed(prices):
            Max = max(Max, n)
            MaxProfit = max(MaxProfit, Max - n)
        return MaxProfit



