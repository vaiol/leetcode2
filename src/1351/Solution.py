from typing import List


class Solution:
    def binarySearch(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (end + start) // 2
            if arr[mid] < 0:
                end = mid - 1
            else:
                start = mid + 1
        return len(arr) - start

    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([self.binarySearch(arr) for arr in grid])
