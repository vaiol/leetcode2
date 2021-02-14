class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def get_directions(row: int, col: int):
            res = []
            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff
                if new_row < 0 or new_row > max_row or new_col < 0 or new_col > max_col:
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                res.append((new_row, new_col))
            return res
        
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        queue = deque()
        grid[0][0] = 1
        queue.append((0, 0))
        
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if row == max_row and col == max_col:
                return distance
            for new_row, new_col in get_directions(row, col):
                grid[new_row][new_col] = distance + 1
                queue.append((new_row, new_col))
        return -1
                    
            
        