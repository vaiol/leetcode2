class Solution:
    def getDistance(self, p1: List[int], p2: List[int]):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        diss = [None] * len(nuts)
        for [i,nut] in enumerate(nuts):
            diss[i] = self.getDistance(tree, nut)
        
        min_dis = float('-inf')
        min_i = 0
        min_s_dis = float('-inf')
        for [i,nut] in enumerate(nuts):
            s_dis = self.getDistance(squirrel, nut)
            curr_dis = (diss[i] * 2) - (diss[i] + s_dis)
            if curr_dis > min_dis:
                min_dis = curr_dis
                min_s_dis = s_dis
                min_i = i
        res = min_s_dis
        print(diss, min_dis, min_i, sum(diss) * 2)
        for i in range(len(diss)):
            if i == min_i:
                res += diss[i]
            else:
                res += diss[i] * 2
        return res
    def minDistanceOpt2(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        max_diff_diss = float('-inf')
        total_diss = 0
        for nut in nuts:
            diss = self.getDistance(tree, nut)
            squirrel_diss = self.getDistance(squirrel, nut)
            total_diss += diss * 2
            max_diff_diss = max(max_diff_diss, (diss * 2) - (diss + squirrel_diss))
        return total_diss - max_diff_diss
                
