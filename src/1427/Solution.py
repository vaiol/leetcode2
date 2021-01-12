from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final_shift = 0
        for d, a in shift:
            if d:
                final_shift += a
            else:
                final_shift -= a
        res = [" "] * len(s)
        for i, c in enumerate(s):
            index = (i + final_shift) % len(s)
            res[index] = c
        return "".join(res)
