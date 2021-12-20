from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        Min = min(m - n for n, m in zip(arr, arr[1:]))
        return [[n, m] for n, m in zip(arr, arr[1:]) if Min == m - n]

    def minimumAbsDifference_2(self, arr: List[int]) -> List[List[int]]:
        #20.12.2021
        arr.sort()

        res = list()
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = abs(arr[i - 1] - arr[i])
            if diff < min_diff:
                min_diff = diff
                res = list()

            if diff == min_diff:
                res.append([arr[i - 1], arr[i]])
        return res
