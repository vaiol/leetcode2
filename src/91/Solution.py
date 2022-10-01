class Solution:
    @lru_cache(maxsize=None)
    def decode_num(self, s: str, i: int) -> int:
        if i == 0:
            return 0 if s[i] == '0' else 1
        is_double = int(s[i - 1 : i + 1]) <= 26
        if i == 1:
            if s[i - 1] == '0':
                return 0
            if s[i] == '0' and int(s[i - 1]) > 2:
                return 0
            return 2 if s[i] != '0' and is_double else 1
        if s[i] == '0' and (int(s[i - 1]) > 2 or s[i - 1] == '0'):
            return 0
        if s[i] == '0':
            return self.decode_num(s, i - 2)
        if s[i - 1] == '0' or not is_double:
            return self.decode_num(s, i - 1)
        return self.decode_num(s, i - 1) + self.decode_num(s, i - 2)
                
            
        