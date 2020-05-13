class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = []
        i = 0
        while i < len(num):
            n = num[i]
            if k > 0 and len(stack) > 0 and int(stack[len(stack) - 1]) > int(n):
                stack.pop(len(stack) - 1)
                k -= 1
            else:
                stack.append(n)
                i += 1

        finalStack = stack[:-k] if k else stack
        return "".join(finalStack).lstrip('0') or "0"

