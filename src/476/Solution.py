class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num).replace("0b", "")
        return int("".join(["0" if n == "1" else "1" for n in binary]), 2)

