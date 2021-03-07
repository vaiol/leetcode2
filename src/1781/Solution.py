class Solution:
    def beautySum(self, s: str) -> int:
        def count(c: Counter) -> int:
            mostCommon = c.most_common()[0]
            leastCommon = c.most_common()[-1]
            return mostCommon[1] - leastCommon[1]

        N = len(s)
        res = 0
        i, j = 0, 2
        while i < N:
            j = i + 3
            c = Counter(s[i:j])
            res += count(c)
            while j < N:
                c[s[j]] += 1
                j += 1
                res += count(c)
            i += 1
        return res
                
                