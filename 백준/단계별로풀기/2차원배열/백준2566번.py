board = [list(map(int, input().split())) for _ in range(9)]

board_max = 0
board_max_row = 0
board_max_col = 0


for i in range(9):
    for j in range(9):
        if board_max <= board[i][j]:
            board_max_row = i+1
            board_max_col = j+1
            board_max = board[i][j]


print(board_max)
print(board_max_row, board_max_col)