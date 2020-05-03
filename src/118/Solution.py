from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(1, numRows + 1):
            arr = [1] * n
            if n == 1 or n == 2:
                res.append(arr)
                continue
            i = 1
            prev = res[n - 2]
            for a1, a2 in zip(prev, prev[1:]):
                arr[i] = a1 + a2
                i += 1
            res.append(arr)
        return res


