from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        summ = 1
        for i, n in enumerate(nums):
            result[i] = summ
            summ *= n

        summ = 1
        for i, n in enumerate(reversed(nums)):
            result[length - i - 1] = result[length - i - 1] * summ
            summ *= n
        return result

    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        # 27.11.2021
        N = len(nums)
        ans = [1] * N

        product = 1
        for i in range(1, N):
            product *= nums[i - 1]
            ans[i] = product

        product = 1
        for i in reversed(range(0, N - 1)):
            product *= nums[i + 1]
            ans[i] = ans[i] * product

        return ans
