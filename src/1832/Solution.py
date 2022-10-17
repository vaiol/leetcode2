class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hash_set = set()
        for ch in sentence:
            hash_set.add(ch)
            if len(hash_set) == 26:
                return True
        return False
        