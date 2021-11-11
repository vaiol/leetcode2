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

    def maxProfitDivideAndConq(self, prices: List[int]) -> int:
        # 10.11.2021
        @lru_cache()
        def rec(start: int, end: int) -> int:
            nonlocal prices
            N = (end + 1) - start
            mid = (end + start) // 2
            if N <= 2:
                return max(0, prices[end] - prices[start])
            return rec(start, mid) + rec(mid, end)

        return rec(0, len(prices) - 1)
