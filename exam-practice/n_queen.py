def print_sol(solutions):
    for solution in solutions:
        for row in solution:
            print(row, end=" | ")
        print()
    print()


def is_safe(board, row, col, n):
    # check if there is queen in same column
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # Check for the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check for the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True # else safe


def solve_nqueen_util(board, row, n, solutions):
    if row == n:
        print_sol(board)
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q' # place queen
            solve_nqueen_util(board, row+1, n, solutions) # recurse
            board[row][col] = '.' # backtrack


def solve_nqueen(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueen_util(board, 0, n, solutions)
    return solutions


n = 4
solutions = solve_nqueen(n)
