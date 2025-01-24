def isValidSudoku(board):
    N = 9

    # Use hash set to record the status
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    print(f'rows - {rows}')
    print(f'cols - {cols}')
    print(f'boxes - {boxes}')

    for r in range(N):
        for c in range(N):
            #print(f'{r},{c}')
            val = board[r][c]
            # Check if the position is filled with number
            if val == ".":
                continue

            # Check the row
            if val in rows[r]:
                return False
            rows[r].add(val)

            # Check the column
            if val in cols[c]:
                return False
            cols[c].add(val)

            # Check the box
            idx = (r // 3) * 3 + c // 3
            if val in boxes[idx]:
                return False
            boxes[idx].add(val)

    return True

board =[["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))