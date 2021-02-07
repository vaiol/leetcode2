class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [None] * len(s)
        cis = []
        for [i, ch] in enumerate(s):
            if ch == c:
                cis.append(i)
                res[i] = 0
        for i in range(len(res)):
            if res[i]:
                continue
            min_dis = float('inf')
            for j in cis:
                min_dis = min(min_dis, abs(j - i))
            res[i] = min_dis
        return res
        