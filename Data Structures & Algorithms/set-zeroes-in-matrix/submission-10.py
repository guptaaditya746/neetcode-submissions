class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[1])
        zeros_items  = []
    
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeros_items.append((i,j))
        for n in zeros_items:
            ## setting rows of mat to zero
            matrix[n] = [0] * col


        for i,j in zero_items:
            matrix[i] = [0] * col
            while i >-1:
                matrix[i][j] = 0
                i = i-1
        return matrix
