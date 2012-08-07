# Gameoflife - generation matrix
from sys import stdout

#Create the generation matrix and return it.
#Input: board 2d matrix
#Output: Next generation board 2d matrix
def generation(board):
    # Get column and row count
    row_len = len(board)
    col_len = len(board[0])

    # Add row padding to 1st and last row of the board
    padding = [0]*col_len
    padded_board = [padding] + board + [padding]

    # Add column padding to first and last column of each row
    for i in range(0,len(padded_board)):
        padded_board[i] = [0] + padded_board[i] + [0]
        
    # Create new board
    new_board = [None] * row_len
    for i in range(0, row_len):
        new_board[i] = [None] * col_len

    # Check for the given conditions and populate the board.
    #TODO: Populate same board and loose the input?
    for row in range(1, row_len + 1):
        for column in range(1, col_len + 1):
            #print padded_board[row][column]
            live_neighbors = padded_board[row-1][column-1] + padded_board[row-1][column] + padded_board[row-1][column + 1] + padded_board[row][column-1]  + padded_board[row][column + 1] + padded_board[row+1][column-1] + padded_board[row+1][column] + padded_board[row+1][column + 1]
            new_value = 0
            if(padded_board[row][column]):
                if live_neighbors == 2 or live_neighbors == 3:
                    new_value = 1
            else:
                if live_neighbors == 3:
                    new_value = 1
            new_board[row-1][column-1] = new_value
            
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
