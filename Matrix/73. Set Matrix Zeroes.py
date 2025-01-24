class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstColFlag = False
        firstRowFlag = False

        # check first column for zero
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                firstColFlag = True
                break
        print(f'Matrix after ith row check - {matrix}')

        # Check first row for zero
        for j in range(len(matrix[0])):
            if matrix[0][j]==0:
                firstRowFlag = True
                break
        print(f'Matrix after jth row check - {matrix}')
        
        # Update zero in corresponding first row and col
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]= 0
                    matrix[i][0] = 0
        print(f'Matrix after row and column - {matrix}')
        
        # Check for zeroes in first col and update that row
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0

         # Check for zeroes in first row and update that col
        for j in range(1,len(matrix[0])):
            if matrix[0][j]==0:
                for i in range(1,len(matrix)):
                    matrix[i][j]=0

        # Check for (0,0) then update first row and column equal to  zero
        if matrix[0][0]==0:
            for i in range(len(matrix)):
                matrix[i][0]=0
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        #...
        if firstRowFlag:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if firstColFlag:
            for i in range(len(matrix)):
                matrix[i][0]=0


"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""