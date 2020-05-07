from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for n in nums:
            if n != val:
                nums[j] = n
                j += 1
        return j

