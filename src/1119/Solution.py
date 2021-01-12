class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        return ''.join(c for c in S if c not in vowels)