from game import *
import re
from copy import deepcopy


def main():
    # Create board object
    board = Board()
    # Pattern for matching regex
    pattern = f"([0-{board.height - 1}],[0-{board.length - 1}])"
    # Select player "O" or "X"
    user = None
    while user not in board.players:
        user = input("Play as 'O' or 'X'?: ")
    # Assign AI to player
    for player in board.players:
        if user != player:
            agent = player
    print("Player 'O' begins first.\n")
    # While game has not ended
    while not board.end_game():
        print(board)
        # If player's turn
        if board.turn == user:
            # Prompt user for coordinate
            move = input(f"Player {user}'s turn:\nMake move (height, length): ")
            # Error-handling
            while not re.fullmatch(pattern, move):
                move = input("Make move (height, length): ")
            board.make_move((int(move[0]), int(move[2])))
        # If AI's turn
        else:
            print(f"AI making move as {agent}...")
            board.make_move(best_move(board))
    # Game ended.
    print(f"Game ended.\n\n{board}")
    if board.end_game() == 2:
        print("Game drawn.\n")
    else:
        if board.end_game() == agent:
            winner = "AI"
        else:
            winner = "User"
        print(f"{winner} won game.\n")


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
    

if __name__ == "__main__":
    main()