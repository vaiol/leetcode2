from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = None
        op = 'buy'
        if len(prices) == 0:
            return 0
        n = prices[0]
        for i in range(1, len(prices)):
            if op == 'buy' and n < prices[i]:
                bought = prices[i - 1]
                op = 'sell'
            elif op == 'sell' and n > prices[i]:
                sold = prices[i - 1]
                profit += sold - bought
                bought = None
                op = 'buy'
            n = prices[i]
        if bought is not None:
            sold = prices[-1]
            profit += sold - bought
        return profit
