from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        def rec(i: int, j: int):
            if i < 0 or i >= len(image):
                return
            if j < 0 or j >= len(image[0]):
                return
            if image[i][j] != oldColor:
                return
            image[i][j] = newColor
            rec(i + 1, j)
            rec(i - 1, j)
            rec(i, j + 1)
            rec(i, j - 1)

        rec(sr, sc)
        return image

