class Solution:
    def maxPower(self, s: str) -> int:
        N = len(s)
        if N < 2:
            return N

        power = 1
        i = 0
        while i < N - power:
            j = 1
            while i + j < N and s[i + j] == s[i]:
                j += 1
            power = max(power, j)
            i += j
        return power
