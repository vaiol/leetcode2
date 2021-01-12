from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for c in ransomNote:
            if not counter.get(c):
                return False
            counter[c] -= 1
        return True
