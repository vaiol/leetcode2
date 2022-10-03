class Solution:
    def minCost1(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) <= 1:
            return len(colors)
        ans = 0
        
        i = 0
        while i < len(colors):
            local_max = 0
            local_sum = 0
            j = i
            while j < len(colors) and colors[i] == colors[j]:
                local_max = max(local_max, neededTime[j])
                local_sum += neededTime[j]
                j += 1

            if j - 1 != i:
                ans += local_sum - local_max

            i = j
            
        return ans
    
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) <= 1:
            return len(colors)
        ans = 0
        local_sum = 0
        local_max = 0
        
        
        i = 0
        while i < len(colors):
            if colors[i] != colors[i - 1]:
                ans += local_sum - local_max
                local_max = 0
                local_sum = 0
            
            local_max = max(local_max, neededTime[i])
            local_sum += neededTime[i]
            i += 1
        
        ans += local_sum - local_max
            
        return ans