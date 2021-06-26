"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

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
    checkx=0
    checko=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                checkx+=1
            elif board[i][j]==O:
                checko+=1
    if checkx>checko:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                Actions.add((i,j))
    return Actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy= deepcopy(board)
    if board_copy[action[0]][action[1]]==EMPTY:
        board_copy[action[0]][action[1]]=player(board)
    else:
        raise NameError("Incorrect move")
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=EMPTY:
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=EMPTY:
            return board[0][i]
    if((board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0]))\
    and (board[1][1]!=EMPTY):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                count+=1
    if count==0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winner_player=winner(board)
    if(Winner_player==X):
        return 1
    elif Winner_player==O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    curr=player(board)
    get_action=None
    if(curr==X):
        v=-math.inf
        for action in actions(board):
            maxvalue=v
            maxvalue=max(maxvalue,MinValue(result(board, action)))
            if maxvalue>v:
                v=maxvalue
                get_action=action
    else: 
        v=math.inf
        for action in actions(board):
            minvalue=v
            minvalue=min(minvalue,MaxValue(result(board, action)))
            if minvalue<v:
                v=minvalue
                get_action=action
    return get_action
    
def MaxValue(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,MinValue(result(board, action)))
    
    return v

def MinValue(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,MaxValue(result(board, action)))
    return v
