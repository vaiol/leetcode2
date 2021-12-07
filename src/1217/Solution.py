class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_count = 0
        even_count = 0
        
        for n in position:
            if n % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        return even_count if even_count < odd_count else odd_count