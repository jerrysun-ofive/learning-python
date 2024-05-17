##########################################################
            ## milestones for this project ##
#   1) Build a data structure to store the board state
#   2) “Pretty-print” the board to the terminal
#   3) Given a starting board state, calculate the next one
#   4) Run the game forever
#   5) Use python curser library to create a good UI
##########################################################

import random
# represent alive cells with 1 and dead cells with 0

# creates a board where every cell is dead
# call this function at the start to get an initial, default board
def dead_state(height: int, width: int):
    new_board = [[0 for i in range(width)] for j in range(height)]
    return new_board

# uses a rng library to determine if a cell is alive or dead to start with
def random_state(board):
    counter = 0
    row_count = 0
    item_count = 0
    for row in board:
        # print(f"row: {row_count}")
        item_count = 0
        for item in row: 
            # print(f"item: {item_count}")
            temp_choice = random.randrange(1, 10)
            if temp_choice < 3:
                board[row_count][item_count] = 1
            item_count += 1
            
        row_count += 1
    return board

# initalise a deafult board
game_board = dead_state(5, 10)
# creates a random 'soup' of cells to start the game
game_board = random_state(game_board)

for row in game_board:
    print(row)