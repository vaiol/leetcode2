class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1
        for row in range(1, ROWS):
            obstacleGrid[row][0] = 1 if obstacleGrid[row][0] == 0 and obstacleGrid[row - 1][0] == 1 else 0

        for col in range(1, COLS):
            obstacleGrid[0][col] = 1 if obstacleGrid[0][col] == 0 and obstacleGrid[0][col - 1] == 1 else 0

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]

        return obstacleGrid[ROWS - 1][COLS - 1]
