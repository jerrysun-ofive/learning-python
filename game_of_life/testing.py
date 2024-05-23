def check_cell_surrounding(board, x, y):
    return_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # print(f"i: {i}, j: {j}")
            return_sum = return_sum + board[x + i][y + j]

    # return sum - 1 because we don't want to include the cell that is getting check
    if board[x][y] == 1: 
        return return_sum - 1
    else:
        return return_sum

def update_cells(board):
    # create a new board to store return board
    return_board = [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ]

    # update all cells that are not edge pieces
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[1]) - 1):
            sum = check_cell_surrounding(board, i, j)
            print(sum)

board = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

update_cells(board)