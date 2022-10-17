class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hash_map = dict()
        
        left, right = 0, 0
        while right < len(s):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            if len(hash_map) > 2:
                hash_map[s[left]] -= 1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left += 1
            right += 1
        return right - left
        