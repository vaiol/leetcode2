class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, N = 0, 0, len(nums)
        if N < 2:
            return N
        while right < N:
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1