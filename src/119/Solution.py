from typing import List


class Solution:
    def __init__(self):
        self.hash = dict()

    def getItemValue(self, row: int, col: int) -> int:
        if col == 0 or col == row or row == 0:
            return 1
        if (row, col) in self.hash:
            return self.hash[(row, col)]
        val = self.getItemValue(row - 1, col - 1) + self.getItemValue(row - 1, col)
        self.hash[(row, col)] = val
        return val

    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        if rowIndex <= 1:
            return row
        for i in range(1, rowIndex):
            row[i] = self.getItemValue(rowIndex, i)
        return row

    def getRowSimple(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        if rowIndex <= 1:
            return row
        prevRow = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            row[i] = prevRow[i - 1] + prevRow[i]
        return row
