class Solution:
    def say(self, s: str) -> str:
        res = []
        count = 1
        ch = s[0]
        for i in range(1, len(s)):
            if ch != s[i]:
                res.extend([str(count), ch])
                ch = s[i]
                count = 1
            else:
                count += 1
        res.extend([str(count), ch])
        return "".join(res)
            
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n - 1))
            
        