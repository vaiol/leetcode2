class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(start: int, end: int, attempt: int):
            if attempt < 0:
                return False
            while start < end:
                if s[start] != s[end]:
                    return checkPalindrome(start + 1, end, attempt - 1) or checkPalindrome(start, end - 1, attempt - 1)
                start += 1
                end -= 1
            return True
        return checkPalindrome(0, len(s) - 1, 1)
