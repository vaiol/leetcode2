class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        if len(jobDifficulty) == d:
            return sum(jobDifficulty)
        
        @lru_cache(maxsize=None)
        def dp(idx: int, maxDificulty: int, d: int) -> int:
            if d > len(jobDifficulty) - idx or idx == (len(jobDifficulty) - 1) and d != 1:
                return float('inf')
            
            current_max_difficulty = max(maxDificulty, jobDifficulty[idx])
            if idx >= (len(jobDifficulty) - 1) and d == 1:
                return current_max_difficulty
            
            # keep seq
            curr_day = dp(idx + 1, current_max_difficulty, d)
            next_day = dp(idx + 1, 0, d - 1) + current_max_difficulty
            # print(idx, curr_day, next_day)
            return min(curr_day, next_day)
        
        return dp(0, 0, d)
        