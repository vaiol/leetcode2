from collections import Counter
from typing import List


class Solution:
    def count(self, word: str, counter: Counter) -> int:
        cp = Counter(word)
        return 0 if cp - counter else len(word)

    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        return sum(self.count(word, Counter(counter)) for word in words)
