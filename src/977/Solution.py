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