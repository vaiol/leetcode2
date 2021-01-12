class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N).replace("0b", "")
        return int("".join(["0" if n == "1" else "1" for n in binary]), 2)