class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mArea = 0
        while left < right:
            mArea = max(mArea, min(height[left], height[right]) * (right - left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return mArea