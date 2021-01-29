class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while right >= left and s[right] == ' ':
            right -= 1
        
        res = []
        while left <= right:
            if s[left] != ' ':
                res.append(s[left])
            elif res[-1] != ' ':
                res.append(' ')
            left += 1
        return res

    def reverseList(self, s: list, left: int, right: int) -> str:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s

    def reverseAllWords(self, s: list) -> str:
        left, right = 0, 0
        
        while left < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            self.reverseList(s, left, right - 1)
            left = right + 1
            right = left
        return s
    
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < len(s) and s[left] == ' ':
            left += 1
        while right >= left and s[right] == ' ':
            right -= 1
        d, word = deque(), []
        while left <= right:
            if s[left] == ' ' and len(word) > 0:
                d.appendleft("".join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))
        
        return ' '.join(d)
        

    def reverseWord2(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverseList(l, 0, len(l) - 1)
        self.reverseAllWords(l)
        return "".join(l)
        
    def reverseWords1(self, s: str) -> str:
        return " ".join(reversed(s.split()))
            