from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        res = []
        anagram = Counter(p)
        counter = Counter()
        for i in range(ns):
            counter[s[i]] += 1
            if i < np - 1:
                continue
            startIndex = i - np + 1
            if counter == anagram:
                res.append(startIndex)
            counter[s[startIndex]] -= 1
            if not counter[s[startIndex]]:
                del counter[s[startIndex]]
        return res
