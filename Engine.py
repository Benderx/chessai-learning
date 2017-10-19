import Piece.py

# -1 will represent black
# 1 will represent white
# init_board will take in optional argument board, and initilize self.board
#            to default position (or to the optional argument if provided)


class Engine():
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]


    def init_board(self, board = None):
        if board:
        	pass
        else:
        	#matt in progress
        	black_rook_1 = Piece.Pawn(-1,)


    def print_final(self):
        for i in self.board:
            print(i)


    def is_terminal(self, color, moves):
        pass


    def get_board(self):
        return self.board


    def push_move(self, move, color):
        self.stack.append(move)
        self.update_board(move,color)


    def pop_move(self):
        move = self.stack.pop()
        self.undo_move(move)


    def update_board(self, move, color):
        pass


    def undo_move(self, move):
        pass


    def valid_move(self, move):
        pass


    def invert_color(self,color):
        return(-color)


    def get_legal_moves(self, color):
        pass