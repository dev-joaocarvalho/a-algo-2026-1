"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action: cell already occupied.")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []
    # Rows and columns
    for k in range(3):
        lines.append([board[k][0], board[k][1], board[k][2]])
        lines.append([board[0][k], board[1][k], board[2][k]])
    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] is not None:
            return line[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current = player(board)

    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best = None
        for action in actions(board):
            score, _ = min_value(result(board, action), alpha, beta)
            if score > v:
                v, best = score, action
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v, best

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best = None
        for action in actions(board):
            score, _ = max_value(result(board, action), alpha, beta)
            if score < v:
                v, best = score, action
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v, best

    if current == X:
        _, action = max_value(board, -math.inf, math.inf)
    else:
        _, action = min_value(board, -math.inf, math.inf)

    return action
