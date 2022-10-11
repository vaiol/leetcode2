class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        prev_row_count = len(mat)
        prev_col_count = len(mat[0])
        
        
        if r * c != prev_row_count * prev_col_count:
            return mat
        
        new_mat = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                index = i * c + j
                prev_row = index // prev_col_count
                prev_col = index % prev_col_count
                new_mat[i][j] = mat[prev_row][prev_col] 
        return new_mat
        