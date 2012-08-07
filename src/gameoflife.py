# Gameoflife - generation matrix

#Create the generation matrix and return it.
#Input: board 2d matrix
#Output: Next generation board 2d matrix
def generation(board):
    # Get column and row count
    row_len = len(board)
    col_len = len(board[0])

    new_board = board
    ##TODO: Perform generation
    
    return new_board

#Print the board in the matrix form
#Input: Board
#Output: None
def printBoard(board):
    row_len = len(board)
    col_len = len(board[0])
    for i in range(0, row_len):
        for j in range(0, col_len):
            stdout.write("%d " % board[i][j])
            stdout.flush()
        stdout.write("\n")
