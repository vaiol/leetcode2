class Solution:
    @lru_cache()
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                d[row][col] = d[row - 1][col] + d[row][col - 1]

        return d[m - 1][n - 1]
