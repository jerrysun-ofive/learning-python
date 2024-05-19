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
            if temp_choice < 4:
                board[row_count][item_count] = 1
            item_count += 1
            
        row_count += 1
    return board

# pretty renders the game onto the terminal
def render(board):
    # prints out the top boarder of the board
    board_outline(board)
    
    # get height and width of the board
    height = len(board)
    width = len(board[1])

    for row in board:
        render_line(row)

    board_outline(board)
                

# prints a line break that represents the boarder of the game
def board_outline(board):
    print("  ", end = "")
    for i in range(len(board[1])):
        print("-  ", end = "")
    print("")

# renders a single line of the board to pretty print
def render_line(row):
    print("|", end = "")
    for i in range(len(row)):
        if row[i] == 1:
            print(" # ", end = "")
        else:
            print("   ", end = "")
    print("|")

# loop through the entire board and update each cell state according
# to the number of cells it is around
def update_cells(board):
    print("test_case")

    

# define the height and width of board
height = 10
width = 10

# initalise a deafult board
game_board = dead_state(height, width)
# creates a random 'soup' of cells to start the game
game_board = random_state(game_board)
#renders the board in terminal 
render(game_board)
