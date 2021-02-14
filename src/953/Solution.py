class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def checkWords(w1: str, w2: str):
            min_len = min(len(w1), len(w2))
            i = 0
            while i < min_len and w1[i] == w2[i]:
                i += 1
            if i == min_len:
                return len(w1) <= len(w2)
            cv1 = order.index(w1[i])
            cv2 = order.index(w2[i])
            return cv1 <= cv2
                
        for i in range(1, len(words)):
            if not checkWords(words[i - 1], words[i]):
                return False
        return True
