from functools import lru_cache


class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        t1, t2 = text1, text2

        @lru_cache(maxsize=None)
        def LCS(i1: int, i2: int) -> int:
            if len(t1) == i1 or len(t2) == i2:
                return 0
            case_remove = LCS(i1 + 1, i2)
            found_index = t2.find(t1[i1], i2)
            if found_index == -1:
                return case_remove
            case_keep = 1 + LCS(i1 + 1, found_index + 1)
            return max(case_remove, case_keep)

        return LCS(0, 0)

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        t1, t2 = text1, text2

        @lru_cache(maxsize=None)
        def LCS(i1: int, i2: int) -> int:
            if len(t1) == i1 or len(t2) == i2:
                return 0
            if t1[i1] == t2[i2]:
                return 1 + LCS(i1 + 1, i2 + 1)
            return max(LCS(i1 + 1, i2), LCS(i1, i2 + 1))

        return LCS(0, 0)

    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for col in reversed(range(n2)):
            for row in reversed(range(n1)):
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]



