class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        gi = 0
        
        i = 0
        while i < len(nums):
            tmp_i = i
            gj = 0
            while i < len(nums) and gj < len(groups[gi]) and groups[gi][gj] == nums[i]:
                i += 1
                gj += 1
            if gj >= len(groups[gi]):
                i -= 1
                gi += 1
                if gi >= len(groups):
                    return True
            else:
                i = tmp_i
            i += 1
        return False
        