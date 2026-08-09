class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[1])
        zeros_items  = {}
    
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeros_items.append({i:j})

        for n in range(zeros_items):
            print(n)
               
        return matrix
