class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9
        SUB_BOX_SIZE = 3
        if len(board) != BOARD_SIZE:
            return False
        if len(board[0]) != BOARD_SIZE:
            return False
        

        def validateRow(row: int):
            arr = [0] * (BOARD_SIZE + 1)
            for i in range(BOARD_SIZE):
                if board[row][i] != '.':
                    num = int(board[row][i])
                    if 1 > num > 9:
                        return False
                    if arr[num] != 0:
                        return False
                    arr[num] += 1
            return True
        
        def validateCol(col: int):
            arr = [0] * (BOARD_SIZE + 1)
            for i in range(BOARD_SIZE):
                if board[i][col] != '.':
                    num = int(board[i][col])
                    if 1 > num > 9:
                        return False
                    if arr[num] != 0:
                        return False
                    arr[num] += 1
            return True
                    
        def validateSubBox(row: int, col: int):
            arr = [0] * (BOARD_SIZE + 1)
            for i in range(SUB_BOX_SIZE):
                for j in range(SUB_BOX_SIZE):
                    if board[row + i][col + j] != '.':
                        num = int(board[row + i][col + j])
                        if 1 > num > 9:
                            return False
                        if arr[num] != 0:
                            return False
                        arr[num] += 1
            return True
                        
        
        
                
        
        for i in range(BOARD_SIZE):
            # validate rows
            if not validateRow(i):
                return False
            # validate cols
            if not validateCol(i):
                return False
            # validate sub-boxes
            row, col = (i // 3) * 3, (i - ((i // 3) * 3)) * 3 
            # print(row, col)
            if not validateSubBox(row, col):
                return False
        return True
            
            