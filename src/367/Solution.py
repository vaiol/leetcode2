class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for n in range(1, num + 1):
            p = n * n
            if p > num:
                break
            if p == num:
                return True
        return False

