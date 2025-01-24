class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashSetRow = set()
        hashSetCol = set()
        # Rows
        print("Sudoku")
        for i in range(9):
            for j in range(9):
                # print(hashSetRow)
                if board[i][j] in hashSetRow and board[i][j] != ".":
                    return False
                if board[j][i] in hashSetCol and board[j][i] != ".":
                    return False

                hashSetRow.add(board[i][j])
                hashSetCol.add(board[j][i])
            print(f'hashSetRow is {hashSetRow} and hashSetCol is {hashSetCol}')
            hashSetRow = set()
            hashSetCol = set()
        
        box1 = set()
        box2 = set()
        box3 = set()

        for k in range(3):
            factor = k*3
            for i in range(3):
                for j in range(3):
 
                    if board[i+factor][j] in box1 and board[i+factor][j] != ".":
                        return False 
                    if board[i+factor][j+3] in box2 and board[i+factor][j+3] != ".":
                        return False
                    if board[i+factor][j+6] in box3 and board[i+factor][j+6] != ".":
                        return False
                    box1.add(board[i+factor][j])
                    box2.add(board[i+factor][j+3])
                    box3.add(board[i+factor][j+6])

            box1 = set()
            box2 = set()
            box3 = set()
        return True
     



"""

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


"""