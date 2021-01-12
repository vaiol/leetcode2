from collections import defaultdict
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        d = defaultdict(int)
        citations_sorted = sorted(citations)
        N = len(citations)
        for i,c in enumerate(reversed(citations_sorted)):
            if c <= i:
                return i
        return N
