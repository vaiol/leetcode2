class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = dict()
        for n in arr:
            N = n * 2
            M = n / 2
            if d.get(N) == True:
                return True
            if n % 2 == 0 and d.get(M) == True:
                return True
            d[n] = True
        return False
            