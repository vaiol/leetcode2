class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prefix_sum = [0] * len(seats)
        
        curr_sum = float('inf')
        for i in reversed(range(len(seats))):
            curr_sum += 1
            if seats[i] == 1:
                curr_sum = 0
            else:
                prefix_sum[i] = curr_sum
        
        ans = 0
        curr_sum = float('inf')
        for i in range(len(seats)):
            curr_sum += 1
            if seats[i] == 1:
                curr_sum = 0
            else:
                ans = max(ans, min(prefix_sum[i], curr_sum))
        return ans
                
        