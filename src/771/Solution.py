class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        Set = set(J)
        return sum(s in Set for s in S)