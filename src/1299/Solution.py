from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        target = [0] * len(arr)
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            target[i] = max_val
            max_val = max(max_val, arr[i])
        return target
    def replaceElements2(self, arr: List[int]) -> List[int]:
        """
        27.01.2021
        """
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp_val = arr[i]
            arr[i] = max_val
            max_val = max(tmp_val, max_val)
        return arr
