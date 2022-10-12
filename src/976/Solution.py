class Solution:
    def check(self, i: int, j: int, k: int) -> int:
        if i + j <= k:
            return 0
        if i + k <= j:
            return 0
        if j + k <= i:
            return 0
        return i + j + k

    def largestPerimeter(self, nums: List[int]) -> int:        
        if len(nums) < 3:
            return 0
        arr = list(reversed(sorted(nums)))
        for i in range(2, len(arr)):
            tmp = self.check(arr[i], arr[i - 1], arr[i - 2])
            if tmp:
                return tmp
        
        return 0
            
            
        
        