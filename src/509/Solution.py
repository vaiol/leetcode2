class Solution:
    def __init__(self):
        self.cache = { 0: 0, 1: 1 }

    def fib2(self, N: int) -> int:
        if (N in self.cache):
            return self.cache[N]
        res = self.fib(N - 1) + self.fib(N - 2)
        self.cache[N] = res
        return res

    def fib(self, N):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)
