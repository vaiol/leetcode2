class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def insertItemArr(arrr, index, num):
            for i in range(len(arrr) - 1, index, -1):
                arrr[i] = arrr[i - 1]
            arrr[index] = num
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                insertItemArr(arr, i, 0)
                i += 1
            i += 1
        