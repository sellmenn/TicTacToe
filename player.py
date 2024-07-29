from game import *
from copy import deepcopy
from time import sleep


# Function to get utility value of board. Return 0 if the game is drawn, 1 if O wins, -1 if X wins.
def get_utility(board):
    winner = board.end_game()
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    return 0


# Function to return best possible move given a board
def best_move(board):
    agent = board.turn 
    moves = board.get_moves()
    if agent == "O":
        utility = -2
        for move in moves:
            brd = deepcopy(board)
            brd.make_move(move)
            value = minvalue(brd)
            if value > utility:
                utility, best = value, move
    else:
        utility = 2
        for move in moves:
            brd = deepcopy(board)
            brd.make_move(move)

            value = maxvalue(brd)
            if value < utility:
                utility, best = value, move
    return best


# Function to return maximum possible utitlity, given a board
def maxvalue(board):
    if board.end_game():
        return get_utility(board)
    utility = -2
    for move in board.get_moves():
        brd = deepcopy(board)
        brd.make_move(move)
        value = minvalue(brd)
        utility = max(value, utility)
    return utility


# Function to return minimum possible utitlity, given a board
def minvalue(board):
    if board.end_game():
        return get_utility(board)
    utility = 2
    for move in board.get_moves():
        brd = deepcopy(board)
        brd.make_move(move)
        value = maxvalue(brd)
        utility = min(value, utility)
    return utility
