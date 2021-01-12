class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        vowels = {'a', 'o', 'i', 'e', 'u'}
        num_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                num_vowels += 1
        maximum = num_vowels
        lo = 0
        for hi in range(k, len(s)):
            if s[hi] in vowels:
                num_vowels += 1
            if s[lo] in vowels:
                num_vowels -= 1
            lo += 1
            maximum = max(maximum, num_vowels)
        return maximum
