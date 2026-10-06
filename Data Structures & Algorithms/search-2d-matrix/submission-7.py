class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n  =len(matrix[0])

        left = 0
        right = m-1

        row = -1

        while left <= right:
            mid = (left + right) //2
            lowest = matrix[mid][0]
            highest = matrix[mid][-1]

            if lowest <= target <= highest:
                row = mid
                break
            elif lowest > target:
                right = mid -1
            else:
                left = mid +1
        
        if row == -1:
            return False

        left = 0
        right = n -1 
        while left <= right:
            mid = (left + right) //2
            val = matrix[row][mid]

            if target == val:
                return True
            elif val > target:
                right = mid -1
            else:
                left = mid +1
        
        return False
            
