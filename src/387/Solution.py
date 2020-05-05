from collections import Counter


class Solution:
    def firstUniqChar2(self, s: str) -> int:
        d = dict()
        for i, c in enumerate(s):
            if c in d:
                d[c] = None
            else:
                d[c] = i
        for c in d:
            if d[c] != None:
                return d[c]
        return -1

    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        return -1
