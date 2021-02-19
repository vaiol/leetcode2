class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x + y:
            return False
        if z == 0:
            return True
        return z % math.gcd(x, y) == 0
        