# UNBEATABLE TIC TAC TOE AI
"Tic-tac-toe (American English), or Xs and Os (Canadian or Irish English) is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner." - Wikepedia

The goal of this project was to write an AI program that could consistently (if not always) beat the user at the game. For simplicity, the project was designed around a text-based Tic-tac-toe game. 

--- 

# HOW TO RUN
1. Ensure all modules in requirements.txt have been installed. Simply use 'pip3 install -r requirements.txt' in your terminal.
2. Type 'python3 player.py' in your terminal. Hit enter. 
3. Squares are configured in rows and columns. To fill the top-left cell, enter '0,0'. To fill the bottom-right cell, enter '2,2'.

# PROJECT DESCRIPTION

This project is based on the Minimax algorithm. In this algorithm, the 'maximizer' tries to get the highest score possible while the 'minimizer' tries to do the opposite and get the lowest score possible. Every state has a value associated with it. In a given state if the maximizer has the upper hand then the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. 

In this project, the maximiser is the player who plays O, and the minimiser is the player who plays X. For a board state where O is the winner, the associated value is 1. For a board state where X is the winner, the associated value is -1. For a drawn board state, the associated value is 0. Thus, the player playing O is trying to 'maximise' the value of the board's state, and the player playing X is trying to 'minimise' the value of the board's state.

The project includes two files: 
1. game.py - contains the **Board** class.
2. player.py - contains the minimax algorithm.

## Board Class
The Board class includes instance methods to simulate a Tic-tac-toe board.

At any point in time, the Board object keeps track of a 3x3 array in self.map representing a Tic-tac-toe board, as well as the current player's turn in self.turn.

Notably, the Board class contains the following instance methods to simulate gameplay.
* self.get_moves() returns a list of empty squares - moves within the confines of the board which have not been filled
* self.end_game() returns the winner of the game O or X, if one exists. If the game is drawn, 2 is returned. If the board is not in a terminal state, False is returned.
* self.make_move() marks a square according to the current player's turn. The current player's turn is automatically updated every time this method is called for convenience.

## player.py

### best_move(board)
This function takes in a Board object as an argument. From there, it is able to determine the current player's turn, and evaluate subsequent playable moves according to the Minimax algorithm. If the current player is O (the maximiser), the function will compare the associated values of the resultant board states for each playable move, and pick the largest possible value. It should be pointed out that the maximiser is assuming that the opponent is playing optimally, hence the maximiser is actualy evaluating the minimum possible value of each board state, and thereafter picking the move which leades to the highest minimum value. Hence, the Minimax algorithm is also recursive by nature.

### maxvalue(board) and minvalue(board)
Both of these functions takes in a Board object as an argument. If the current board state is terminal, the associated 'utility' value of the state is returned, 0 for a drawn game, 1 if O has won, and -1 if X has won. Otherwise, the functions will make deep copies of the Board object, and use them to evaulate subsequent moves. This is so as to prevent altering the actual Board object used in the terminal interface. Similar to the best_move function, the maxvalue function will call on the minvalue function and pick the highest possible minimum value. In contrast, the minvalue function will call on the maxvalue function and pick the lowest possible maximum value.

