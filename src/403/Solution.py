class Solution:
    @lru_cache(maxsize=None)
    def canCrossRec(self, stones: tuple[int], i: int, units: int) -> bool:
        if i == len(stones) - 1:
            return True
        max_units = units + 1
        min_units = units - 1
        
        min_required_units = stones[i + 1] - stones[i]
        if min_required_units > max_units:
            return False
        
       
        possible_moves = []

        curr_i = i + 1
        while curr_i < len(stones) and stones[curr_i] - stones[i] <= max_units:
            if stones[curr_i] - stones[i] >= min_units:
                possible_moves.append(curr_i)
            curr_i += 1
        if len(possible_moves) == 0:
            return False
        if possible_moves[-1] == len(stones) - 1:
            return True
        
        for move_i in reversed(possible_moves):
            if self.canCrossRec(stones, move_i, stones[move_i] - stones[i]):
                return True
        return False
            
        
        
        
            
    def canCross(self, stones: List[int]) -> bool:
        return self.canCrossRec(tuple(stones), 0, 0)
        