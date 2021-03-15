class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] < 0 and (not res or res[-1] < 0):
                res.append(asteroids[i])
            elif asteroids[i] < 0 and res and res[-1] > 0 and res[-1] == abs(asteroids[i]):
                res.pop()
            elif asteroids[i] < 0 and res and res[-1] > 0 and res[-1] < abs(asteroids[i]):
                while res and res[-1] > 0 and res[-1] < abs(asteroids[i]):
                    res.pop()
                i -= 1
            elif asteroids[i] > 0:
                res.append(asteroids[i])
            i += 1
        return res
            
            
            
            
            