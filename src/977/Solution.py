class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        iRes = len(nums) - 1
        i, j = 0, len(nums) - 1
        while i <= j:
            iN = abs(nums[i])
            jN = abs(nums[j])
            N = None
            if iN > jN:
                i += 1
                N = iN
            else:
                j -= 1
                N = jN
            res[iRes] = pow(N, 2)
            iRes -= 1
        return res
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        i_res = len(nums) - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                val = pow(nums[left], 2)
                left += 1
            else:
                val = pow(nums[right], 2)
                right -= 1
            res[i_res] = val
            i_res -= 1
        return res
