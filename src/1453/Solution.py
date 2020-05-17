from cmath import acos, sqrt
from math import atan2
from typing import List


class Solution:
    def __init__(self):
        self.distances = None

    def getDistances(self, points: List[List[int]]) -> None:
        N = len(points)
        self.distances = [[0] * N for i in range(N)]
        for i in range(N - 1):
            for j in range(i + 1, N):
                x1,y1 = points[i]
                x2,y2 = points[j]
                dis = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
                self.distances[i][j] = self.distances[j][i] = abs(dis)
    
    def getPointsInside(self, i: int, r: int, points: List[List[int]]) -> int:
        N = len(points)
        angles = []
        for j in range(N):
            if i != j and self.distances[i][j] <= 2*r:
                x1,y1 = points[i]
                x2,y2 = points[j]
                
                B = acos(self.distances[i][j] / (2*r))
                A = atan2(y2 - y1, x2 - x1)
                alpha = A - B
                beta = A + B
                angles.append([alpha, True])
                angles.append([beta, False])
        angles.sort(key=lambda x: (x[0], -x[1]))
        count, res = 1, 1
        for a in angles:
            if a[1]:
                count += 1
            else:
                count -= 1
            res = max(count, res)
        return res

    def numPoints(self, points: List[List[int]], r: int) -> int:
        N = len(points)
        self.getDistances(points)
        ans = 1
        for i in range(N):
            ans = max(ans, self.getPointsInside(i, r, points))
        return ans
