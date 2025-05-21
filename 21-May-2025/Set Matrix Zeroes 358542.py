# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        rows = len(matrix)
        columns = len(matrix[0])

        for row in range(rows):
            for column in range(columns):
                if matrix[row][column]==0:
                    res.append((row,column))

        for i,k in res:
            for column in range(columns):
                matrix[i][column]= 0
            
            for row in range(rows):
                matrix[row][k]=0
