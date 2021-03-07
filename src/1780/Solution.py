class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        MAX = 10 ** 7
        nums = [1]
        curr_num = 3
        i = 2
        while curr_num <= n:
            nums.append(curr_num)
            curr_num = 3 ** i
            i += 1
        
        print(nums)
        @lru_cache(maxsize=None)
        def dfs(i: int, s: int):
            if s > n:
                return False
            if s == n:
                return True
            if i >= len(nums):
                return False
            return dfs(i + 1, s) or dfs(i + 1, s + nums[i])
        return dfs(0, 0)
            
            