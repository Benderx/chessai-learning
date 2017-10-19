import Piece.py

# -1 will represent black
# 1 will represent white
# init_board will take in optional argument board, and initilize self.board
#            to default position (or to the optional argument if provided)
# Position is in (x,y)

class Engine():
    def __init__(self):
    	#Board is accessed using [y][x] notation
        self.board = [[None for x in range(8)] for y in range(8)]


    def init_board(self, board = None):
        if board:
        	pass
        else:
        	black_pawn_1 = Piece.Pawn(-1,(0,6))
        	black_pawn_2 = Piece.Pawn(-1,(1,6))
        	black_pawn_3 = Piece.Pawn(-1,(2,6))
        	black_pawn_4 = Piece.Pawn(-1,(3,6))
        	black_pawn_5 = Piece.Pawn(-1,(4,6))
        	black_pawn_6 = Piece.Pawn(-1,(5,6))
        	black_pawn_7 = Piece.Pawn(-1,(6,6))
        	black_pawn_8 = Piece.Pawn(-1,(7,6))
        	self.board[6][0] = black_pawn_1
        	self.board[6][1] = black_pawn_2
        	self.board[6][2] = black_pawn_3
        	self.board[6][3] = black_pawn_4
        	self.board[6][4] = black_pawn_5
        	self.board[6][5] = black_pawn_6
        	self.board[6][6] = black_pawn_7
        	self.board[6][7] = black_pawn_8

        	white_pawn_1 = Piece.Pawn(1,(0,1))
        	white_pawn_2 = Piece.Pawn(1,(1,1))
        	white_pawn_3 = Piece.Pawn(1,(2,1))
        	white_pawn_4 = Piece.Pawn(1,(3,1))
        	white_pawn_5 = Piece.Pawn(1,(4,1))
        	white_pawn_6 = Piece.Pawn(1,(5,1))
        	white_pawn_7 = Piece.Pawn(1,(6,1))
        	white_pawn_8 = Piece.Pawn(1,(7,1))
        	self.board[1][0] = white_pawn_1
        	self.board[1][1] = white_pawn_2
        	self.board[1][2] = white_pawn_3
        	self.board[1][3] = white_pawn_4
        	self.board[1][4] = white_pawn_5
        	self.board[1][5] = white_pawn_6
        	self.board[1][6] = white_pawn_7
        	self.board[1][7] = white_pawn_8

        	black_rook_1 = Piece.Rook(-1,(0,7))
        	black_rook_2 = Piece.Rook(-1,(7,7))
        	self.board[7][0] = black_rook_1
        	self.board[7][7] = black_rook_2

        	white_rook_1 = Piece.Rook(1,(0,0))
        	white_rook_2 = Piece.Rook(1,(7,0))
        	self.board[0][0] = white_rook_1
        	self.board[0][7] = white_rook_2

        	black_knight_1 = Piece.Knight(-1,(1,7))
        	black_knight_2 = Piece.Knight(-1,(6,7))
        	self.board[7][1] = black_knight_1
        	self.board[7][6] = black_knight_2

        	white_knight_1 = Piece.Knight(1,(1,0))
        	white_knight_2 = Piece.Knight(1,(6,0))
        	self.board[0][1] = white_knight_1
        	self.board[0][6] = white_knight_2

        	black_bishop_1 = Piece.Bishop(-1,(2,7))
        	black_bishop_2 = Piece.Bishop(-1,(5,7))
        	self.board[7][2] = black_bishop_1
        	self.board[7][5] = black_bishop_2

        	white_bishop_1 = Piece.Bishop(1,(2,0))
        	white_bishop_2 = Piece.Bishop(1,(5,0))
        	self.board[0][2] = white_bishop_1
        	self.board[0][5] = white_bishop_2

        	black_king = Piece.King(-1,(3,7))
        	black_queen = Piece.Queen(-1,(4,7))
        	self.board[7][3] = black_king
        	self.board[7][4] = black_queen

        	white_king = Piece.King(1,(3,0))
        	white_queen = Piece.Queen(1,(4,0))
        	self.board[0][3] = white_king
        	self.board[0][4] = white_queen


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


    def get_possible_squares(self, piece):
        if piece.get_piece() == 'Pawn':
            pass
        if piece.get_piece() == 'Rook':
            pass
        elif piece.get_piece() == 'Knight':
            pass
        elif piece.get_piece() == 'Bishop':
            pass
        elif piece.get_piece() == 'Queen':
            pass
        elif piece.get_piece() == 'King':
            pass


    def get_legal_moves(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.get_color == color:
                    moves += get_possible_squares(piece)
