##########################################################
            ## milestones for this project ##
#   1) Build a data structure to store the board state
#   2) “Pretty-print” the board to the terminal
#   3) Given a starting board state, calculate the next one
#   4) Run the game forever
#   5) Use python curser library to create a good UI
##########################################################

#represent alive cells with 1 and dead cells with 0

def dead_state(height: int, width: int):
    new_board = [[0]*width]*height
    return new_board

return_board = dead_state(5, 10)

for row in return_board:
    print(row)