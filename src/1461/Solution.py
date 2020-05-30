class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = 2**k
        for i in range(l):
            p = bin(i)[2:].rjust(k, '0')
            if p not in s:
                return False
        return True
