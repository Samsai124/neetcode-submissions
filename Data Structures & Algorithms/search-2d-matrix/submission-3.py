class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target > matrix[i][len(matrix[i])-1]:
                continue
            elif target == matrix[i][len(matrix[i])-1]:
                return True
            else:
                for val in matrix[i]:
                    if val == target:
                        return True
                return False
        return False