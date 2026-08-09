class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        # spiral_array = []
        # matrix.size = m, n
        # for row in range(m):
        #     if row // 2 == 0:
        #         spiral_array.append(row)
        #     else:
        #         spiral_array.append(row[-1])
        # return spiral_array
        a = [1,2,3]
        temp = []
        for i in range(-1,1,1):
            temp.append(a[i])
        return temp

        ## how to write row
        # row1 = matrix[0],
        # row2 = matrix[1]
        # row3 = matrix[1][-1:0]