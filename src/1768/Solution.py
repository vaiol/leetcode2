class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ["0"] * (len(word1) + len(word2))
        i_word = 0
        i = 0
        while i_word < len(word1) or i_word < len(word2):
            if i_word < len(word1):
                res[i] = word1[i_word]
                i += 1  
            if i_word < len(word2):
                res[i] = word2[i_word]
                i += 1 
            i_word += 1
        
        return "".join(res)