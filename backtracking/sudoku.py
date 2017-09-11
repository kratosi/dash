

def get_value(board, row, col):
    if board[row][col] != 0:
        return board[row][col]

    for i in range(1, 10):
        valid = True
        for j in range(len(board)):
            if board[row][j] == i:
                valid = False
                break

            if board[j][col] == i:
                valid = False
                break


        ir = (row / 3) * 3
        ic = (col / 3) * 3

        for j in range(ir, ir + 3):
            for k in range(ic, ic + 3):
                if board[j][k] == i:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            return i

    return -1


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
    n = get_value(board, row, col)
    if n == -1:
        return False

    board[row][col] = n
    print row,col
    print_board(board)
    x ,y = get_next_cell(row, col, len(board))
    if play(board, x, y):
        return True
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
