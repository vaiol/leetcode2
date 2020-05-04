from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            summ = numbers[low] + numbers[high]
            if summ == target:
                return [low + 1, high + 1]
            elif summ < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]



