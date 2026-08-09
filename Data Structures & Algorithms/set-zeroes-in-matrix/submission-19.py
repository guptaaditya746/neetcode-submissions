class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[1])
        zeros_items  = []
    
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeros_items.append((i,j))
   


        for i,j in zeros_items:
            matrix[i] = [0] * col
            rows = row -1
            while rows >-1:
                matrix[rows][j] = 0
                rows = rows-1
        
