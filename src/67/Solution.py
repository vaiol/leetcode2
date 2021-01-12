class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def toSt(arr):
            return ''.join(map(str, arr))

        maxLen = max(len(a), len(b)) + 1
        res = [0] * maxLen
        ai = len(a) - 1
        bi = len(b) - 1
        i = maxLen - 1
        n = 0
        while i >= 0:
            an = int(a[ai]) if ai >= 0 else 0
            bn = int(b[bi]) if bi >= 0 else 0
            n, sm = (an + bn + n) // 2, (an + bn + n) % 2
            res[i] = sm
            i -= 1
            ai -= 1
            bi -= 1
        return toSt(res[1:]) if res[0] == 0 else toSt(res)



