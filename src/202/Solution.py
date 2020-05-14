from typing import List


class Solution:
    def __init__(self):
        self.n = 0

    def itoa(self, n: int) -> List[int]:
        res = []
        while n > 0:
            res.append(n % 10)
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        arr = self.itoa(n)
        res = 0
        for num in arr:
            res += pow(num, 2)
        self.n += 1
        if self.n > 500:
            return False
        return True if res == 1 else self.isHappy(res)


