class Solution:
    def multiply(self, num1: str, num2: str) -> str:  
        if num1 == "0" or num2 == "0": 
            return "0"
    
        n1 = num1[::-1]
        n2 = num2[::-1]

        res = [0] * (len(n1) + len(n2))
        
        def addToNumByIndex(amount: int, index: int):
            nonlocal res
            new_val = res[index] + amount
            if new_val < 10:
                res[index] = new_val
            else:
                res[index] = new_val % 10
                addToNumByIndex(new_val // 10, index + 1)
        
        i1 = 0
        i2 = 0
        for i1 in range(len(n1)):
            for i2 in range(len(n2)):
                val = int(n1[i1]) * int(n2[i2])
                addToNumByIndex(val, i1 + i2)
        
        i = len(res) - 1
        while res[i] == 0 and i > 0:
            i -= 1
        return "".join(map(str, reversed(res[0:i + 1])))