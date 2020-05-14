from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        Min = min(m - n for n, m in zip(arr, arr[1:]))
        return [[n, m] for n, m in zip(arr, arr[1:]) if Min == m - n]
