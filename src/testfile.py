# Test file
from sys import stdout
import gameoflife
            
def readFromFile(myFile):
    matrix = []
    f = open(myFile,"r")
    lines = f.readlines()
    f.close()
    for line in lines:
        matrix = matrix + [[int(x) for x in line.split(' ')]]
    return matrix

def test_case_compare(inputFile, cheatFile):
    inp = readFromFile(inputFile)
    stdout.write("Input Board\n")
    myObj = gameoflife.GameOfLife()
    myObj.printBoard(inp)
    out = myObj.generation(inp)
    if(out):
        stdout.write("Output Board\n")
        myObj.printBoard(out)
        ans = readFromFile(cheatFile)
        if ans == out:
            stdout.write("\nTest Passed. Hurray! :-)")
        else:
            stdout.write("\nTest Failed. I screwed up :-(")

