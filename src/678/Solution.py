class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'
        L, R = 0, 0
        for n in s:
            if n in LEFTY:
                L += 1
            else:
                L -= 1
            if L < 0:
                return False
        if L == 0:
            return True

        for n in reversed(s):
            if n in RIGHTY:
                R += 1
            else:
                R -= 1
            if R < 0:
                return False
        return True

