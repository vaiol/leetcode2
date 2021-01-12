class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            tmp = mid * mid
            if tmp == x:
                return mid
            if tmp > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1 if left else left
