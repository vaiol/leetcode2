from typing import List


class Solution:
    def singleNonDuplicate_1(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (end + start) // 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
        return nums[start] if start % 2 == 0 else nums[start - 1]

    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (end + start) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid - 1
        return nums[start]


