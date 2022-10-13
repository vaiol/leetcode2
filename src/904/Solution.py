class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        left, right = 0, 0
        d = dict()
        while right < len(fruits):
            # print(len(d), d)
            if len(d) > 2 or (len(d) == 2 and fruits[right] not in d):
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
            if fruits[right] not in d:
                d[fruits[right]] = 0
            d[fruits[right]] += 1
            right += 1
            
        return right - left
            
            
        