class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if len(picture) == 0:
            return 0
        if len(picture[0]) == 0:
            return 0
        rows = [-1] * len(picture)
        columns = [-1] * len(picture[0])
        
        for col in range(len(columns)):
            row_id = -1
            for row in range(len(rows)):
                if picture[row][col] == 'B':
                    if row_id != -1:
                        row_id = -1
                        break
                    row_id = row
            if row_id != -1:
                columns[col] = row_id    
            
        ans = 0

        for row in range(len(rows)):
            col_id = -1
            for col in range(len(columns)):
                if picture[row][col] == 'B':
                    if col_id != -1:
                        col_id = -1
                        break
                    col_id = col
            if col_id != -1 and columns[col_id] != -1:
                ans += 1
        return ans
                
                
                
            