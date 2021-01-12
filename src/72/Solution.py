from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = word1, word2
        @lru_cache(maxsize=None)
        def LCS(i1: int, i2: int) -> int:
            if i1 == len(w1) and i2 == len(w2):
                return 0
            elif i1 == len(w1) or i2 == len(w2):
                return max(len(w1) - i1, len(w2) - i2)
            if w1[i1] == w2[i2]:
                return LCS(i1 + 1, i2 + 1)
            case1 = 1 + LCS(i1 + 1, i2 + 1)
            case2 = 1 + LCS(i1 + 1, i2)
            case3 = 1 + LCS(i1, i2 + 1)
            return min(case1, case2, case3)
        return LCS(0, 0)
