class Solution:
    def reverseL(self, l: list, left: int, right: int):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
    def reverseWords(self, s: str) -> str:
        l = list(s)
        n = len(l) - 1
        left, right = 0, 0
        while left < len(l) and l[left] == ' ':
            left += 1
        while n > 0 and l[n] == ' ':
            n -= 1
        while right <= n:
            if l[right] == ' ':
                self.reverseL(l, left, right - 1)
                left = right + 1
            right += 1
        self.reverseL(l, left, right - 1)
        return "".join(l)