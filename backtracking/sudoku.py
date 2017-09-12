def valid_cell(board, row, col):
    if board[row][col] == 0:
        return True
    return False


def can_set_value(board, row, col, val):
    #if board[row][col] != 0:
    #    return False

    #for i in range(1, 10):
    #    valid = True
    for j in range(len(board)):
        if board[row][j] == val:
            return False

        if board[j][col] == val:
            return False


    ir = (row / 3) * 3
    ic = (col / 3) * 3

    for j in range(ir, ir + 3):
        for k in range(ic, ic + 3):
            if board[j][k] == val:
                return False

    return True


def get_next_cell(row, col, limit):
    col = col + 1
    if col >= limit:
        col = 0
        row += 1
    return row, col


def play(board, row, col):
    if row > len(board) - 1:
        return True

    #for i in range(len(board)):
    #    for j in range(len(board)):

    print "before" ,row,col

    if not valid_cell(board, row, col):
        x ,y = get_next_cell(row, col, len(board))
        if play(board, x, y):
            return True
    else:
        print "Valid cell ", row, col
        for val in range(1,10): 
            cs = can_set_value(board, row, col, val)
            #if n == -1:
            #    return False
            if not cs:
                continue

            board[row][col] = val
            print row,col
            print_board(board)
            x ,y = get_next_cell(row, col, len(board))
            if play(board, x, y):
                return True
            if cs:
                board[row][col] = 0

    return False


def print_board(board):
    print "=" * 80
    for i in range(len(board)):
        for j in range(len(board)):
            if j % 3 == 0:
                print "|",
            print board[i][j], " ",
        if (i+1) % 3 == 0:
            print
            for j in range(len(board)*2 + 3):
                print "-",
        print

    print "=" * 80


def main():
    board = [[3,0,6,5,0,8,4,0,0],
             [5,2,0,0,0,0,0,0,0],
             [0,8,7,0,0,0,0,3,1],
             [0,0,3,0,1,0,0,8,0],
             [9,0,0,8,6,3,0,0,5],
             [0,5,0,0,9,0,6,0,0],
             [1,3,0,0,0,0,2,5,0],
             [0,0,0,0,0,0,0,7,4],
             [0,0,5,2,0,6,3,0,0]]

    play(board, 0, 1)
    print_board(board)

main()

