#!/usr/bin/python3
"""
N queens problem
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the
    given position (row, col) on the board.
    """
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in enumerate(range(row - 1, -1, -1)):
        if board[j] == col - i - 1:
            return False

    for i, j in enumerate(range(row - 1, -1, -1)):
        if board[j] == col + i + 1:
            return False

    return True


def solve_nqueens(board, row, n):
    """
    Recursively solve the N Queens problem
    and print every possible solution.
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def main() -> None:
    """
    Entry point to the program.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    main()
