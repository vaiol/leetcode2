from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rmin = [min(x) for x in matrix]
        cmax = [max(x) for x in zip(*matrix)]
        return [n for n in cmax if n in rmin]
