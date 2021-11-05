class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        left, right = 0, n - 1
        while right >= left:
            mid = left + (right - left) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            if curr > n:
                right = mid - 1
            if curr < n:
                left = mid + 1
        return right