class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0
        while i < N - 1 and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == N - 1:
            return False
            
        while i < N - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        return i == N - 1
