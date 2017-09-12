
moves_x = [1, 1, 2, 2, -1, -1, -2, -2]
moves_y = [2, -2, 1, -1, 2, -2, 1, -1]

N = 5

def can_move(board, row, col):
    if (row>=0 and row<=N-1) and (col>=0 and col<=N-1) and board[row][col] == 0:
        return True
    else:
        return False

def knight(board, row, col, mc):
    global moves_x, moves_y

    if mc == N * N + 1:
        return True

    for i in range(len(moves_x)):
        if can_move(board, row, col):
            board[row][col] = mc
            print_board(board)
            next_x = row + moves_x[i]
            next_y = col + moves_y[i]

            if knight(board, next_x, next_y, mc+1):
                return True

            board[row][col] = 0

def print_board(board):
    print "-" *50
    for r in board:
        print r
    print "-" *50


def main():
    board = []

    for i in range(N):
        l = []
        for j in range(N):
            l.append(0)
        board.append(l)

    knight(board, 0, 0, 1)
    print "== FINAL =="
    print_board(board)

main()

