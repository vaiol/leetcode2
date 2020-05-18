from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        c1, c2 = Counter(s1), Counter(s2[:l1])
        for i in range(l1, l2):
            if c1 == c2:
                return True
            c2[s2[i]] += 1
            c2[s2[i - l1]] -= 1
            if c2[s2[i - l1]] == 0:
                del c2[s2[i - l1]]
        return c1 == c2
 