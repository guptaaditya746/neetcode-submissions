class Solution:


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        spiral_array = []
        m = len(matrix)  
        for row in range(m):
            if row % 2 == 0:
                spiral_array.append(matrix[row])
            else:
                spiral_array.append((matrix[row]).reverse())
        return spiral_array

     

        

        ## how to write row
        # row1 = matrix[0],
        # row2 = matrix[1]
        # row3 = matrix[1][-1:0]