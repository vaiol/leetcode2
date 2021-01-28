class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        flipped_count = 0
        max_count = 0
        for n in nums:
            if n == 0:
                max_count = max(flipped_count, max_count)
                flipped_count = count + 1
                count = 0
            else:
                flipped_count += 1
                count += 1
        return max(flipped_count, max_count)