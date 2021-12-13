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

    def maxPower1(self, s: str) -> int:
        #13.12.2021
        N = len(s)
        if N <= 1:
            return N

        res = 1
        curr_n = 1
        for i in range(1, N):
            if s[i] != s[i - 1]:
                res = max(res, curr_n)
                curr_n = 0
            curr_n += 1
        return max(res, curr_n)

