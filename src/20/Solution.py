class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')', 
            '{': '}',
            '[': ']'
        }
        stack = []
        for parenthes in s:
            if parenthes in parentheses:
                stack.append(parenthes)
            elif not stack or parentheses[stack.pop()] != parenthes:
                return False
        return True if len(stack) == 0 else False
        