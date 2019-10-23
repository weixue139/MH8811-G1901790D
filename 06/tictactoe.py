#06 H2 program tictactoe module    by Wei Xue

#Module to print a tic-tac-toe board:

#Supporting functions:
#Function to print horizontal seperation lines of length n:
def printLine_hori(n):
    for i in range(n):
        print('-', end = '')
    print('')
#Function to print cell content depending on list value:
def printCell(cell):
    if cell == 0:
        print(' O ', end = '')
    elif cell == 1:
        print(' X ', end = '')
    else:
        print('   ', end = '')
#Function to print vertical separation lines:        
def printLine_vert():
    print('|', end = '')
        
#Function to draw a tic-tac-toe board, where board is a list of list:
def TicTacDraw(board):
    #get length of first row and check if it is a square:
    board_len = len(board)
    for i in range(board_len):
        if len(board[i]) != board_len:
            print('board is not square!')
            return
        for j in range(board_len):
            if board[i][j] not in [0,1,2]:
                print('not valid value!')
                return           
      
    #print board:
    for i in range(board_len):
        for j in range(board_len):
            printCell(board[i][j])
            if j<board_len-1:
                printLine_vert()
            else:
                print('')
        if i<board_len-1:
            printLine_hori(board_len*4-1)
    
#If the module is run as a main program:
if __name__ == "__main__":
    #print out a default board of length 3x3:
    board = [ [ 0, 1, 2 ], [ 2, 0, 0 ], [ 1, 1, 2 ] ]
    TicTacDraw(board)