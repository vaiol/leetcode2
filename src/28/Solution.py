class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, H = len(needle), len(haystack)
        if len(needle) == 0:
            return 0
        i = 0
        while i < H - N + 1:
            while i < H - N + 1 and haystack[i] != needle[0]:
                i += 1
            j = 0
            while j < N and i + j < H and haystack[i + j] == needle[j]:
                j += 1
            if j == N:
                return i
            print(i, H)
            i += 1
        return -1
