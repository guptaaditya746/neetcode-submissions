class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        spiral_array = []
        len(matrix) == m      
        for row in range(m):
            if row // 2 == 0:
                spiral_array.append(matrix[row])
            else:
                spiral_array.append(reverse_array(matrix[row]))
        return spiral_array

     

        def reverse_array(arra: List[int]) -> List[int]:
            temp = []
            for i in range(len(arra), -1, -1):
                temp.append(temp[arra[i]])

            
            return temp

        ## how to write row
        # row1 = matrix[0],
        # row2 = matrix[1]
        # row3 = matrix[1][-1:0]