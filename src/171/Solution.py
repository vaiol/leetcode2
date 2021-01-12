class Solution:
    def titleToNumber(self, s: str) -> int:
        d = dict()
        j = 1
        for i in range(ord('A'), ord('Z')+1):
            d[chr(i)] = j
            j = j + 1
        summ = 0
        q = 26
        for i in range(len(s) - 2, -1, -1):
            print(i)
            summ = summ + d[s[i]] * q
            q *= 26
        summ += d[s[-1]]
        return summ