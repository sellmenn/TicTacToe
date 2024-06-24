class Board:
    def __init__(self):
        self.height = 3
        self.length = 3
        self.map = self.get_map(self.height, self.length)
        self.players = ["O", "X"]
        self.turn = "O"

    def __repr__(self):
        return_str = ""
        x = 0
        for row in self.map:
            return_str += f"{x}{row}\n"
            x += 1
        return return_str

    def get_map(self, height, length):
        map = []
        for i in range(height):
            map.append(list())
            for j in range(length):
                map[i].append(list())
        return map
    
    def make_move(self, square):
        height, length = square
        if not self.map[height][length]:
            self.map[height][length].append(self.turn)
            for player in self.players:
                if self.turn != player:
                    self.turn = player
                    return True
        else:
            print("Square is already filled.")
            return False
        
    def get_turn(self):
        return self.turn
    
    # Function to check if game is over or has been won. Return winner "O", "X", 2 if game is drawn, or False if game is not over
    def end_game(self):
        # Check for horizontal wins
        for row in self.map:
            if row[0] == row[1] and row[1] == row[2] and row[0]:
                return row[0][0]
        # Check for vertical wins
        for i in range(3):
            if self.map[0][i] == self.map[1][i] and self.map[1][i] == self.map[2][i] and self.map[0][i]:
                return self.map[0][i][0]
        # Check for diagonal wins
        if self.map[0][0] == self.map[1][1] and self.map[1][1] == self.map[2][2] and self.map[0][0]:
            return self.map[0][0][0]
        elif self.map[2][0] == self.map[1][1] and self.map[1][1] == self.map[0][2] and self.map[2][0]:
            return self.map[2][0][0]
        # Check for empty squares
        for row in self.map:
            for square in row:
                if not square:
                    return False
        return 2
    
    def get_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if not self.map[i][j]:
                    moves.append((i,j))
        return moves
     

