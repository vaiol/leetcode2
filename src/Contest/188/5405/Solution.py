from typing import List


# 1442
# Count Triplets That Can Form Two Arrays of Equal XOR
# https://stackoverflow.com/questions/57839761/find-the-number-of-triplets-i-j-k-in-an-array-such-that-the-xor-of-elements-inde
# https://www.geeksforgeeks.org/number-of-triplets-in-array-having-subarray-xor-equal/

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 0
        for i in range(N):
            cumm = 0
            for j in range(i, N):
                cumm ^= arr[j]
                if cumm == 0:
                    print(i, j)
                    ans += j - i
        return ans

S = Solution()
print(S.countTriplets([2,3,1,6,7]))



