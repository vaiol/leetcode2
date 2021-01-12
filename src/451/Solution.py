from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res = []
        for letter, freq in c.most_common():
            res.append(letter * freq)
        return "".join(res)
