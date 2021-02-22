class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubsequance(str_full: str, str_sub: str) -> bool:
            i = 0
            for c in str_full:
                if c == str_sub[i]:
                    i += 1
                    if i == len(str_sub):
                        return True
            return False
        
        res = ""
        for sub in d:
            if isSubsequance(s, sub):
                if len(sub) > len(res) or (len(sub) == len(res) and sub < res):
                    res = sub
        return res
