class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        c = Counter(nums)
        for cc in c:
            if c[cc] > 1:
                res += c[cc] * (c[cc] - 1) // 2
        return res
