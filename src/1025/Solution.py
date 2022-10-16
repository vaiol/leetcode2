class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        if n == 2:
            return True
        
        @lru_cache(maxsize=None)
        def dp(num: int, is_alice_move: bool) -> bool:
            # print(num, is_alice_move)
            if num == 1:
                return not is_alice_move
            if num == 2:
                return is_alice_move

            for x in range(1, num):
                if is_alice_move and num % x == 0 and dp(num - x, not is_alice_move):
                    return True
                if not is_alice_move and num % x == 0 and not dp(num - x, not is_alice_move):
                    return False
            return False if is_alice_move else True
        
        return dp(n, True)
                
        