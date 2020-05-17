from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = list(map(set, favoriteCompanies))
        res = []
        for i,n in enumerate(sets):
            issubset = True
            for j,k in enumerate(sets):
                if i != j and n.issubset(k):
                    issubset = False
                    break
            if issubset:
                res.append(i)
        return res
