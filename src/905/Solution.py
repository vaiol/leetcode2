class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] % 2 == 0:
                left += 1
            elif A[right] % 2 == 1:
                right -= 1
            else:
                tmp = A[left]
                A[left] = A[right]
                A[right] = tmp
                left += 1
                right -= 1
        return A
            
        