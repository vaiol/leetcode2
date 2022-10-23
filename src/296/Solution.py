class Solution:
    
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def getDistance1D(pointers: List[int], median: int) -> int:
            res = 0
            for point in pointers:
                res += abs(point - median)
            return res
        
        rows = list()
        cols = list()
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    rows.append(row)
        
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    cols.append(col)
        
        medianRow = rows[len(rows) // 2]
        medianCol = cols[len(cols) // 2]
        return getDistance1D(rows, medianRow) + getDistance1D(cols, medianCol)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def minTotalDistanceBFS(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])

        friends = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    friends.append((i, j))
                    grid[i][j] = 0
                    
        
        def getNeighbours(i: int, j: int, visited: set):
            neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            res = []
            for iDiff, jDiff in neighbours:
                newI = i - iDiff
                newJ = j - jDiff
                if newI >= 0 and newJ >= 0 and newI < rowCount and newJ < colCount and (newI, newJ) not in visited:
                    res.append((newI, newJ))
            return res
                
        def calcDistance(i: int, j: int) -> int:
            visited = set()
            queue = deque()
            queue.append((i, j, 0))
            visited.add((i, j))
            minDis = float('inf')
            while queue:
                row, col, distance = queue.popleft()
                grid[row][col] += distance
                minDis = min(minDis, grid[row][col])
                for newRow, newCol in getNeighbours(row, col, visited):
                    queue.append((newRow, newCol, distance + 1))
                    visited.add((newRow, newCol))
            return minDis
            
        

        for i in range(1, len(friends)):
            row, col = friends[i]
            calcDistance(row, col)
        
        minAfterLastFriend = calcDistance(friends[0][0], friends[0][1])

        return minAfterLastFriend
                    
                    
                    
                
                
            
        