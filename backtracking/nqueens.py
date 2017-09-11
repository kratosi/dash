
def can_move(row, col, board):
    """
    The queen can move only if there is no
    other queen horizontally, vertically or
    diagonally
    """

    for i in range(len(board)):
        if board[row][i] ==1 or board[i][col] == 1:
            return False

    for i in range(len(board)):
        for j in range(len(board)):
            if i+j == row+col and board[i][j] == 1:
                return False

            if i-j == row-col and board[i][j] == 1:
                return False

    return True


def queens(n, board):
    if n == 0:
        return True

    for i in range(len(board)):
        for j in range(len(board)):
            if can_move(i,j,board):
                board[i][j] = 1
                if queens(n-1, board):
                    return True
                board[i][j] = '.'

    return False


def initialize(n, board):
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append('.')


def print_board(n, board):
    for i in range(n):
        print board[i]


def main():
    n = 8
    board = []
    initialize(n ,board)
    queens(n, board)
    print_board(n, board)



main()

