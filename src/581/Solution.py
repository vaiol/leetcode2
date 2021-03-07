class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)
        start, end = 0, len(snums) - 1
        while start < len(snums) and nums[start] == snums[start]:
            start += 1
        while end >= 0 and nums[end] == snums[end]:
            end -= 1
        return 0 if start >= end else end - start + 1