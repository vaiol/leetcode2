class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if not sentence:
            return -1
        if not searchWord:
            return 0
        words = sentence.split(' ')
        for i,w in enumerate(words):
            if w.startswith(searchWord):
                return i + 1
        return -1
