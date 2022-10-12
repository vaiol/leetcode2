class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        if matrix[0][0] > target:
            return False
        
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        
       
        row = right
        
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
        