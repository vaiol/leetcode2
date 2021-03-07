class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = Counter(candyType)
        return len(c) if len(c) <= len(candyType) // 2 else len(candyType) // 2
        