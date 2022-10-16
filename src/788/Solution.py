class Solution:
    def rotatedDigits(self, n: int) -> int:
        goodNumbers = {2, 5, 6, 9}
        badNumbers = {3, 4, 7}
        def numberIsGood(num: int) -> bool:
            isGood = False
            while num:
                mod = num % 10
                if mod in badNumbers:
                    return False
                if mod in goodNumbers:
                    isGood = True
                num //= 10
            return isGood
        ans = 0
        for i in range(1, n + 1):
            if numberIsGood(i):
                ans += 1
        return ans
        