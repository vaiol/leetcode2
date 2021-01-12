from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(list)
        for a, b in prerequisites:
            d[a].append(b)

        @lru_cache(maxsize=None)
        def dfs(a: int, b: int) -> bool:
            if a == b:
                return True
            return any(dfs(n, b) for n in d[a])
                
        return [dfs(a, b) for a, b in queries]
