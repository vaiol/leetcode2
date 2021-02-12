class Solution:
    def check(self, nums: List[int]) -> bool:
        firstNum = nums[0]
        lastNum = nums[-1]
        isPeak = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if isPeak:
                    return False
                else:
                    isPeak = True
        if isPeak:
            return firstNum >= lastNum
        else:
            return True
