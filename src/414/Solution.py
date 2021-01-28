class Solution:
    def thirdMax1(self, nums: List[int]) -> int:
        third, second, first = float('-inf'), float('-inf'), float('-inf')
        for n in nums:
            if n > first:
                third = second
                second = first
                first = n
            elif n == first:
                first = n
            elif n > second:
                third = second
                second = n
            elif n == second:
                second = n
            elif n > third:
                third = n
            print(n, first, second, third)
        return third if third > float('-inf') else first
        
    def thirdMax(self, nums: List[int]) -> int:

        # Make a Set with the input.
        nums = set(nums)

        # Find the maximum.
        maximum = max(nums)

        # Check whether or not this is a case where
        # we need to return the *maximum*.
        if len(nums) < 3:
            return maximum

        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)