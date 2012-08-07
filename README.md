gameoflife
==========

Create generation matrix for a given input

ASSUMPTIONS:
1) "Clean" input given in a file. The file path along with the file name given as input to the function call.
2) The board does not fold over (Bottom row being neighbor of the top row etc).

LOGIC:
1) Add pad rows and columns around the board.
2) n^2 algorithm to iterate through each cell and find out the neighbor count and thus the resulting next generation matrix.

HOW TO RUN THE CODE:
From python command prompt: (Assuming the directory if created has been added to the path)
import testfile
test_case_compare("input1.txt","ans1.txt") # assuming both files are in the current working directory
