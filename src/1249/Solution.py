class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = []
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
                l.append(c)
            elif c == ')':
                if balance > 0:
                    balance -= 1
                    l.append(c)
            else:
                l.append(c)
        res = []
        balance = 0
        for c in reversed(l):
            if c == ')':
                balance += 1
                res.append(c)
            elif c == '(':
                if balance > 0:
                    balance -= 1
                    res.append(c)
            else:
                res.append(c)
        return "".join(reversed(res))
            
        