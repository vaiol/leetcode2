from typing import List


class Solution:
    def singleNonDuplicate_2(self, nums: List[int]) -> int:
        # 20.11.2021
        left, right = 0, len(nums) - 2
        while left < right:
            mid = left + (right - left) // 2
            isEven = mid % 2 == 0
            isOdd = mid % 2 == 1
            if (isEven and nums[mid] == nums[mid + 1]) or (isOdd and nums[mid] != nums[mid + 1]):
                left = mid + 1
            elif (isEven and nums[mid] != nums[mid + 1]) or (isOdd and nums[mid] == nums[mid + 1]):
                right = mid - 1
        return nums[right] if right % 2 == 0 else nums[right + 1]

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


