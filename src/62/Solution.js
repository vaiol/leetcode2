/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    d = Array(m).fill(Array(n).fill(1))
    for (let i = 1; i < d.length; i++) {
        for (let j = 1; j < d[i].length; j++) {
            d[i][j] = d[i - 1][j] + d[i][j - 1]
        }
    }
    return d[m - 1][n - 1]
};