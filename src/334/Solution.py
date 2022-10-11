class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = nums[0]
        second_num = float('inf')
        for i in range(1, len(nums)):
            if nums[i] < first_num:
                first_num = nums[i]
            if nums[i] > first_num and nums[i] < second_num:
                second_num = nums[i]
            if nums[i] > second_num:
                return True
        return False