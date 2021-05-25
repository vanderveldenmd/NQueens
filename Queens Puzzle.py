answers = []
n = 9
import copy

def tryToPlaceInRow(pastBoard, board, row):
    rowSnapshot = board[row]
    queenCol = 0
    curNumOpen = findNumOpen(rowSnapshot)
    if curNumOpen == 0:
        board= resetBoard(board)
        row -= 1
        return
    elif row == len(board) - 1:
        board, queenCol = findLastOpen(board, row)
        board = placeQueen(board, row, queenCol)
        recordAnswer(board)
        removeQueen(board, row)
        board[row][queenCol] = 1
    else:
        for j in range(0, len(rowSnapshot)):
            if rowSnapshot[j] == 0:
                board = placeQueen(board, row, j)
                tryToPlaceInRow(pastBoard, board, row + 1)
                if findQueenInRow(board[row]) != -1:
                    board, queenCol = removeQueen(board, row)
                    board = resetBoard(board)
        if row == 0:
            return
        if findQueenInRow(board[row]) == -1:
            board, queenCol = removeQueen(board, row - 1)
            board = resetBoard(board)
            row -= 1
        else:
            board, queenCol = removeQueen(board, row )
            board = resetBoard(board)
        curNumOpen = findNumOpen(board[row])
        row -= 1
        rowSnapshot = board[row]
    return


def placeQueen(board, row, col):
    board[row][col] = 'Q'
    for i in range(len(board)):
        if board[row][i] != 'Q':
            board[row][i] += 1
    for j in range(len(board)):
        if board[j][col] != 'Q':
            board[j][col] += 1
    n = 1
    while row + n < len(board) and col + n < len(board):
        board[row + n][col + n] += 1
        n += 1
    n = 1
    while row - n >= 0 and col + n < len(board):
        board[row - n][col + n] += 1
        n += 1
    n = 1
    while row + n < len(board) and col - n >= 0:
        board[row + n][col - n] += 1
        n += 1
    n = 1
    while row - n >= 0 and col - n >= 0:
        board[row - n][col - n] += 1
        n += 1    
    return board

def resetBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'Q':
                board[i][j] = 0
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'Q':
                placeQueen(board, i, j)
    return board

def resetRow(boardRow):
    for i in boardRow:
        if i == -1:
            i = 0
    return

def removeQueen(board, row):
    for i in range(len(board)):
        if board[row][i] != 'Q':
            board[row][i] -= 1
        else:
            col = i
    for j in range(len(board)):
        if board[j][col] != 'Q':
            board[j][col] -= 1
    n = 1
    while row + n < len(board) and col + n < len(board):
        board[row + n][col + n] -= 1
        n += 1
    n = 1
    while row - n > 0 and col + n < len(board):
        board[row - n][col + n] -= 1
        n += 1
    n = 1
    while row + n < len(board) and col - n > 0:
        board[row + n][col - n] -= 1
        n += 1
    n = 1
    while row - n > 0 and col - n > 0:
        board[row - n][col - n] -= 1
        n += 1  
    board[row][col] = 1  
    return board, col

def findQueenInRow(boardRow):
    for i in range(len(boardRow)):
        if boardRow[i] == 'Q':
            return i
    return -1
    
def findNumOpen(boardRow):
    numOpen = 0
    for i in boardRow:
        if i == 0:
            numOpen += 1
    return numOpen

def findLastOpen(board, row):
    for i in range(len(board)):
        if board[row][i] == 0:
            board[row][i] = 'Q'
            return board, i
    return board, i


    
def recordAnswer(board):
    doSomething = 0
    answers.append(copy.deepcopy(board))
    if len(answers) == 2:
        doSomething = 1
    return

def printSolutions():
    printableSolutions = []
    lineSolution = []
    lineStr = ''
    for count in answers:
        for i in count:
            for j in i:
                if j == 'Q':
                    lineStr += j
                else:
                    lineStr += '*'
            lineSolution.append(lineStr)
            lineStr = ''
        printableSolutions.append(lineSolution)
    print(printableSolutions)


board = [[0 for i in range(n)] for j in range(n)]
pastBoard = []
tryToPlaceInRow(pastBoard, board, 0)

printSolutions()
print("The number of solutions for n = ", n, " is ", len(answers))

