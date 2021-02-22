/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
const uniquePathsWithObstacles = function(obstacleGrid) {
  const M = obstacleGrid.length;
  const N = obstacleGrid[0].length;

  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (obstacleGrid[i][j] === 1) {
        obstacleGrid[i][j] = 0;
      } else if (i === 0 && j === 0) {
        obstacleGrid[i][j] = 1;
      } else if (i === 0) {
        obstacleGrid[i][j] = obstacleGrid[i][j - 1];
      } else if (j === 0) {
        obstacleGrid[i][j] = obstacleGrid[i - 1][j];
      } else {
        obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1];
      }
    }
  }
  return obstacleGrid[M - 1][N - 1];
};
