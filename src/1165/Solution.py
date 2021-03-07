class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        m = dict()
        for i,ch in enumerate(keyboard):
            m[ch] = i
        
        res = 0
        last_index = 0
        for ch in word:
            res += abs(last_index - m[ch])
            last_index = m[ch]
        return res