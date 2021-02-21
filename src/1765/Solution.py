class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        M = len(isWater)
        N = len(isWater[0])
        
        res = [None] * M
        
        queue = deque()
        
        for i in range(M):
            res[i] = [None] * N
            for j in range(N):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        while queue:
            x, y = queue.popleft()
            distance = res[x][y]

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N and (res[new_x][new_y] == None or res[new_x][new_y] > distance + 1):
                    res[new_x][new_y] = distance + 1
                    queue.append((new_x, new_y))
                
        
        return res
