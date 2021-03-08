from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        ss = set(s)
        for w in ss:
            for i in range(1, len(w)):
                word_to_remove = w[i:]
                if word_to_remove in s:
                    s.remove(word_to_remove)
        return sum(len(w) + 1 for w in s)
