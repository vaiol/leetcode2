from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        unique_numbers = set()
        res = []
        for denominator in range(1, n + 1):
            for numerator in range(1, denominator):
                tmp = numerator / denominator
                if tmp not in unique_numbers:
                    unique_numbers.add(tmp)
                    res.append(f"{numerator}/{denominator}")
        return res
