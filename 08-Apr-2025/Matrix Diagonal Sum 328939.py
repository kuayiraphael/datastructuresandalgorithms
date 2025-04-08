# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)


        def sumOfPrimaryDiagonal(mat):
            total=0
            for i in range(n):
                total += mat[i][i]
            return total
        
        def sumOfSecondaryDiagonal(mat):
            total = 0
            k=n-1
            for i in range(n):
                    total += mat[i][k-i]
            return total
        

        

        primaryDiagonalSum = sumOfPrimaryDiagonal(mat)
        secondaryDiagonalSum = sumOfSecondaryDiagonal(mat)
        print(secondaryDiagonalSum)
        print(primaryDiagonalSum)
        diagonalSum = primaryDiagonalSum + secondaryDiagonalSum

        if len(mat)%2==1:
            return diagonalSum - mat[(len(mat)-1)//2][(len(mat)-1)//2]
        return diagonalSum


        