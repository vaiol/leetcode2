class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #17.12.2021
        if not matrix or not matrix[0]:
            return 0
        N = len(matrix)
        M = len(matrix[0])
        res = 0
        
        
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i][j] == '0':
                    continue
                matrix[i][j] = min(int(matrix[i - 1][j]), int(matrix[i][j - 1]), int(matrix[i - 1][j - 1])) + 1
        
        for i in range(N):
            for j in range(M):
                res = max(res, int(matrix[i][j]))

        return res * res
