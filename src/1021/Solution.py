class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        opened_p = '('

        arr = []
        counter = 0
        for p in s:
            if p == opened_p:
                if counter != 0:
                    arr.append(p)
                counter += 1
            else:
                if counter != 1:
                    arr.append(p)
                counter -= 1
        return "".join(arr)
                    
        