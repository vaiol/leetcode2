class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def dis(x1, x2, y1, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        min_id = -1
        min_dis = float('inf')
        for i,p in enumerate(points):
            if x == p[0] or y == p[1]:
                curr_dis = dis(x, p[0], y, p[1])
                if curr_dis < min_dis:
                    min_id = i
                    min_dis = curr_dis
        return min_id