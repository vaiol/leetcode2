from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colors = dict()

        def dfs(curr: int, color: bool):
            if curr in colors:
                return colors[curr] == color
            colors[curr] = color
            return all(dfs(dis, not color) for dis in graph[curr])

        return all(dfs(i, True) for i in range(1, N + 1) if i not in colors)
