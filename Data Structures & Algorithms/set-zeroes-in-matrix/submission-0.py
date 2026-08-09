class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row , col = size(matrix)
        for i in range(row):
            for j in range(col):
                if  matrix[i][j] == 0 :
                    matrix[i] = 0 * col
                    matrix[j] = 0 * row
                

        return matrix
               