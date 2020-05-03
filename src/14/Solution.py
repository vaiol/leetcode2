class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        if n == 1:
            return strs[0]
        res = ''
        i = 0
        while i < 100:
            for j in range(1, n):
                if len(strs[j - 1]) <= i or len(strs[j]) <= i or strs[j - 1][i] != strs[j][i]:
                    return res
            res += strs[0][i]
            i += 1
        return res
