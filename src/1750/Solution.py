class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        if len(s) == 1:
            return 1
        if len(s) == 2 and s[left] != s[right]:
            return 2
        if len(s) == 2 and s[left] == s[right]:
            return 0
            
        
        while left < right:
            while left < right and s[left] == s[right]:
                left += 1
            while left <= right and left > 0 and s[right] == s[left - 1]:
                right -= 1
            if s[left] != s[right]:
                break
        return 0 if left > right else right - left + 1
