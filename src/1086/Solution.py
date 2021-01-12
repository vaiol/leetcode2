import bisect
from collections import defaultdict
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dd = defaultdict(list)
        for student, score in items:
            bisect.insort(dd[student], score)
        return [[student, sum(dd[student][-5:])//5] for student in dd]
