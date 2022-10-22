class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        counter_len = len(counter)
        left, right = 0, 0
        
        ans = (-1,-1)
        min_len = float('inf')
        curr_counter = Counter()
        while right < len(s):
            curr_counter[s[right]] = curr_counter.get(s[right], 0) + 1
            right += 1
            while not (counter - curr_counter):
                curr_len = right - left
                if curr_len < min_len:
                    min_len = curr_len
                    ans = (left, right)
                curr_counter[s[left]] -= 1
                left += 1
        # print(min_len, ans)
        if ans == (-1, -1):
            return ""
        return s[ans[0]:ans[1]]

        