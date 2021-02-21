class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def checkIfNice(s: str):
            c = Counter(s)
            m = {}
            for ch in c:
                if ch.islower() and ch.upper() not in c:
                    return False
                if ch.isupper() and ch.lower() not in c:
                    return False
            return True
            
        max_len = 0
        max_str = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    continue
                st = s[i:j + 1]
                # print(st)
                if checkIfNice(st) and len(st) > max_len:
                    max_len = len(st)
                    max_str = st
        return max_str
        