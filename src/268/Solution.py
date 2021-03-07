class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        N = len(nums)

        null_exist = False
        for i,n in enumerate(nums):
            index = abs(n)
            if index < N and nums[index] > 0:
                nums[index] = -nums[index]
            if index < N and nums[index] == 0:
                null_exist = True

        for i,n in enumerate(nums):
            if n > 0:
                return i
            if n == 0 and not null_exist:
                return i
        return N

    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expected = N * (N + 1) // 2
        return expected - sum([n for n in nums])