class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) -1

        while left <= right:
            mid = int((left + right)/2)
            midRow = matrix[mid] 
            if midRow[0] <=target<=midRow[-1]:
                # binary searach
                return self.binary(midRow,target)
            elif midRow[0] > target:
                right = mid -1
            else:
                left = mid +1
        return False
    def binary(self, array, target):
        left = 0
        right = len(array)

        while left <= right:
            mid = int((left + right)/2)
            if array[mid] < target:
                left = mid +1
            elif array[mid] > target:
                right = mid -1
            else:
                return True
        return False
