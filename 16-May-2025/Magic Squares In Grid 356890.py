# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        validNumbers = {1,2,3,4,5,6,7,8,9}
        count = 0

        for row in range(n-2):
            for column in range(m-2):
                primaryDiagonalSum = 0
                secondaryDiagonalSum = 0
                row1Sum = 0
                row2Sum = 0
                row3Sum = 0
                column1Sum = 0
                column2Sum = 0
                column3Sum = 0
                res = set()

                for i in range(3):
                    for j in range(3):
                        res.add(grid[row+i][column+j])

                        if i==0:
                            row1Sum +=grid[row+i][column+j]
                        if i == 1:
                            row2Sum +=grid[row+i][column+j]
                        if i==2:
                            row3Sum +=grid[row+i][column+j]
                            
                        if j==0:
                            column1Sum +=grid[row+i][column+j]
                        if j == 1:
                            column2Sum +=grid[row+i][column+j]
                        if j==2:
                            column3Sum +=grid[row+i][column+j]

                        if i==j:
                            primaryDiagonalSum +=grid[row+i][column+j]
                        
                        if (i==1 and j ==1) or (i==2 and j==0) or (i==0 and j==2):
                            secondaryDiagonalSum += grid[row+i][column+j]

                if secondaryDiagonalSum==primaryDiagonalSum==row1Sum==row2Sum==row3Sum==column1Sum==column2Sum==column3Sum and res == validNumbers:
                    count+=1
        return count



