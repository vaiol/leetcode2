from collections import defaultdict
from typing import List


class Solution:
    def findJudge1(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        citizens = set()
        trusted_citizens = set()
        d = defaultdict(list)
        for citizen, trust_in in trust:
            d[trust_in].append(citizen)
            trusted_citizens.add(trust_in)
            citizens.add(citizen)
        potential_judges = trusted_citizens - citizens
        final_judge = None
        for judge in potential_judges:
            if set(d[judge]) == citizens:
                if final_judge:
                    return -1
                final_judge = judge
        return final_judge if final_judge else -1
