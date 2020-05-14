from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        iOdds = 0
        iEvens = 1
        for n in A:
            if (n % 2 == 0):
                res[iOdds] = n
                iOdds += 2
            else:
                res[iEvens] = n
                iEvens += 2
        return res
