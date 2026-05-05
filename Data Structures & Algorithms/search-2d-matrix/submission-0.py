class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #rows
        n = len(matrix[0]) #coloums
        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid//n][mid%n]
            if mid_value == target:
                return True
            if mid_value < target:
                left = mid + 1
            if mid_value > target:
                right = mid - 1
        return False
