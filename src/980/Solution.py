class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        start_row, start_col = 0, 0
        non_obstacles_count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    start_row, start_col = row, col
                if grid[row][col] >= 0:
                    non_obstacles_count += 1
        path_count = 0
        
        def backtrack(row, col, remain):
            nonlocal path_count
            if grid[row][col] == 2:
                if remain == 1:
                    path_count += 1
                return
            
            prev_cell_val = grid[row][col]
            grid[row][col] = remain * -1
            
            for ri, ci in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_row = row + ri
                new_col = col + ci
                if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS:
                    continue
                if grid[new_row][new_col] < 0:
                    continue
                backtrack(new_row, new_col, remain - 1)
            
            
            grid[row][col] = prev_cell_val
        
        backtrack(start_row, start_col, non_obstacles_count)
        
        return path_count
