from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for a,b in prerequisites:
            d[a].append(b)
        path = []
        @lru_cache(maxsize=None)
        def detectCycle(i) -> bool:
            nonlocal path
            if i in path:
                path = []
                return False
            path.append(i)
            return all(detectCycle(n) for n in d[i])
        return all(detectCycle(i) for i in range(numCourses))
