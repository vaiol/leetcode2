class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [True if n + extraCandies >= M else False for n in candies]