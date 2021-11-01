class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        ROWS = len(board)
        COLS = len(board[0])
        
        ROW_FIRST_ID = 0
        ROW_LAST_ID = ROWS - 1
        COL_FIRST_ID = 0
        COL_LAST_ID = COLS - 1
        
        def DFS(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            if board[i][j] != 'O':
                return
            board[i][j] = '1'

            DFS(i, j - 1)
            DFS(i, j + 1)
            DFS(i - 1, j)
            DFS(i + 1, j)
        
        

        for i in range(COLS):
            if board[ROW_FIRST_ID][i] == 'O':
                DFS(ROW_FIRST_ID, i)
            if board[ROW_LAST_ID][i] == 'O':
                DFS(ROW_LAST_ID, i)
        
        for i in range(ROWS):
            if board[i][COL_FIRST_ID] == 'O':
                DFS(i, COL_FIRST_ID)
            if board[i][COL_LAST_ID] == 'O':
                DFS(i, COL_LAST_ID)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
            