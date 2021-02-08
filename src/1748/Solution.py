class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        c = Counter(nums)
        for k in c:
            if c[k] == 1:
                res += k
        return res