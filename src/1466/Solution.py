from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        d = defaultdict(list)
        dr = defaultdict(list)
        for a,b in connections:
            d[a].append(b)
            dr[b].append(a)
        count = 0
        stack = [0]
        visited = set()
        while len(stack) > 0:
            root = stack.pop(0)
            r1 = [n for n in dr[root] if n not in visited]
            r2 = [n for n in d[root] if n not in visited]
            stack += r1
            stack += r2
            count += len(r2)
            visited.add(root)
        return count
