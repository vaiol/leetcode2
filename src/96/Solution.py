class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        d = [0] * (n + 1)
        d[0], d[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                d[i] += d[j - 1] * d[i - j]
        return d[n]

    @lru_cache()
    def numTreesRec(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        s = 0
        for i in range(1, n + 1):
            s += self.numTreesRec(i - 1) * self.numTreesRec(n - i)
        return s
