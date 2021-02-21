class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        currY = Y
        while currY > X:
            if currY % 2 != 0:
                currY += 1
            else:
                currY //= 2
            count += 1
        return X - currY + count
        