import Piece

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
            #Custom board state
            pass
        else:
            #Initialize basic chess board
            self.board[6][0] = Piece.Pawn(1,(0,6))
            self.board[6][1] = Piece.Pawn(1,(1,6))
            self.board[6][2] = Piece.Pawn(1,(2,6))
            self.board[6][3] = Piece.Pawn(1,(3,6))
            self.board[6][4] = Piece.Pawn(1,(4,6))
            self.board[6][5] = Piece.Pawn(1,(5,6))
            self.board[6][6] = Piece.Pawn(1,(6,6))
            self.board[6][7] = Piece.Pawn(1,(7,6))

            black_pawn_1 = Piece.Pawn(-1,(0,1))
            black_pawn_2 = Piece.Pawn(-1,(1,1))
            black_pawn_3 = Piece.Pawn(-1,(2,1))
            black_pawn_4 = Piece.Pawn(-1,(3,1))
            black_pawn_5 = Piece.Pawn(-1,(4,1))
            black_pawn_6 = Piece.Pawn(-1,(5,1))
            black_pawn_7 = Piece.Pawn(-1,(6,1))
            black_pawn_8 = Piece.Pawn(-1,(7,1))
            self.board[1][0] = black_pawn_1
            self.board[1][1] = black_pawn_2
            self.board[1][2] = black_pawn_3
            self.board[1][3] = black_pawn_4
            self.board[1][4] = black_pawn_5
            self.board[1][5] = black_pawn_6
            self.board[1][6] = black_pawn_7
            self.board[1][7] = black_pawn_8

            white_rook_1 = Piece.Rook(1,(0,7))
            white_rook_2 = Piece.Rook(1,(7,7))
            self.board[7][0] = white_rook_1
            self.board[7][7] = white_rook_2

            black_rook_1 = Piece.Rook(-1,(0,0))
            black_rook_2 = Piece.Rook(-1,(7,0))
            self.board[0][0] = black_rook_1
            self.board[0][7] = black_rook_2

            white_knight_1 = Piece.Knight(1,(1,4))
            white_knight_2 = Piece.Knight(1,(6,7))
            self.board[4][1] = white_knight_1
            self.board[7][6] = white_knight_2

            black_knight_1 = Piece.Knight(-1,(1,0))
            black_knight_2 = Piece.Knight(-1,(6,0))
            self.board[0][1] = black_knight_1
            self.board[0][6] = black_knight_2

            white_bishop_1 = Piece.Bishop(1,(2,7))
            white_bishop_2 = Piece.Bishop(1,(5,7))
            self.board[7][2] = white_bishop_1
            self.board[7][5] = white_bishop_2

            black_bishop_1 = Piece.Bishop(-1,(2,0))
            black_bishop_2 = Piece.Bishop(-1,(5,0))
            self.board[0][2] = black_bishop_1
            self.board[0][5] = black_bishop_2

            white_king = Piece.King(1,(3,7))
            white_queen = Piece.Queen(1,(4,7))
            self.board[7][3] = white_king
            self.board[7][4] = white_queen

            black_king = Piece.King(-1,(3,0))
            black_queen = Piece.Queen(-1,(4,0))
            self.board[0][3] = black_king
            self.board[0][4] = black_queen


    def print_board(self):
        for row in self.board:
            a = []
            for col in row:
                if col == None:
                    a.append(' ')
                else:
                    if col.get_color() == 1:
                        a.append(col.get_piece()[0].lower())
                    else:
                        a.append(col.get_piece()[0].upper())
            print(a)

    def in_check(self, color):
        #Takes in color of player's turn
        #Ensures they do not end turn in check
        if color == -1:
            pos = black_king.get_position()
        else:
            pos = white_king.get_position()

        #Check to left of king
        for i in range(pos[0]-1,-1,-1):
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


    def invert_color(self,color):
        return(-color)


    def get_possible_squares(self, piece):
        moves = []
        pos = piece.get_position()
        init_x = pos[0]
        init_y = pos[1]
        piece_name = piece.get_piece()


        if piece_name == 'Pawn':
            pass

        elif piece_name == 'Rook':
            for y in range(1, 8):
                if init_y + y > 7:
                    break
                space = self.board[init_y + y][init_x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x, init_y + y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x, init_y + y)))
                    break

            for y in range(1, 8):
                if init_y - y < 0:
                    break
                space = self.board[init_y - y][init_x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x, init_y - y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x, init_y - y)))
                    break

            for x in range(1, 8):
                if init_x + x > 7:
                    break
                space = self.board[init_y][init_x + x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x + x, init_y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x + x, init_y)))
                    break

            for x in range(1, 8):
                if init_x - x < 0:
                    break
                space = self.board[init_y][init_x - x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x - x, init_y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x - x, init_y)))
                    break

        elif piece_name == 'Night':
            x_1 = init_x + 1
            y_1 = init_y - 2
            if x_1 < 8 and y_1 > -1:
                space = self.board[y_1][x_1]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_1, y_1)))

            x_2 = init_x + 2
            y_2 = init_y - 1
            if x_2 < 8 and y_2 > -1:
                space = self.board[y_2][x_2]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_2, y_2)))

            x_3 = init_x + 2
            y_3 = init_y + 1
            if x_3 < 8 and y_3 < 8:
                space = self.board[y_3][x_3]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_3, y_3)))

            x_4 = init_x + 1
            y_4 = init_y + 2
            if x_4 < 8 and y_4 < 8:
                space = self.board[y_4][x_4]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_4, y_4)))

            x_5 = init_x - 1
            y_5 = init_y + 2
            if x_5 > -1 and y_5 < 8:
                space = self.board[y_5][x_5]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_5, y_5)))

            x_6 = init_x - 2
            y_6 = init_y + 1
            if x_6 > -1 and y_6 < 8:
                space = self.board[y_6][x_6]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_6, y_6)))

            x_7 = init_x - 2
            y_7 = init_y - 1
            if x_7 > -1 and y_7 > -1:
                space = self.board[y_7][x_7]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_7, y_7)))

            x_8 = init_x - 1
            y_8 = init_y - 2
            if x_8 > -1 and y_8 > -1:
                space = self.board[y_8][x_8]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_8, y_8)))

        elif piece_name == 'Bishop':
            for inc in range(1, 8):
                if init_x + inc > 7 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x + inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x + inc, init_y + inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x + inc, init_y + inc)))
                    break

            for inc in range(1, 8):
                if init_x + inc > 7 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x + inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x + inc, init_y - inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x + inc, init_y - inc)))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x - inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x - inc, init_y + inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x - inc, init_y + inc)))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x - inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x - inc, init_y - inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x - inc, init_y - inc)))
                    break

        elif piece_name == 'Queen':
            for y in range(1, 8):
                if init_y + y > 7:
                    break
                space = self.board[init_y + y][init_x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x, init_y + y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x, init_y + y)))
                    break

            for y in range(1, 8):
                if init_y - y < 0:
                    break
                space = self.board[init_y - y][init_x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x, init_y - y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x, init_y - y)))
                    break

            for x in range(1, 8):
                if init_x + x > 7:
                    break
                space = self.board[init_y][init_x + x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x + x, init_y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x + x, init_y)))
                    break

            for x in range(1, 8):
                if init_x - x < 0:
                    break
                space = self.board[init_y][init_x - x]

                if space is None:
                    moves.append(((init_x, init_y), (init_x - x, init_y)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x - x, init_y)))
                    break


            for inc in range(1, 8):
                if init_x + inc > 7 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x + inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x + inc, init_y + inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x + inc, init_y + inc)))
                    break

            for inc in range(1, 8):
                if init_x + inc > 7 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x + inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x + inc, init_y - inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x + inc, init_y - inc)))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x - inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x - inc, init_y + inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x - inc, init_y + inc)))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x - inc]

                if space is None:
                    moves.append(((init_x, init_y), (init_x - inc, init_y - inc)))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(((init_x, init_y), (init_x - inc, init_y - inc)))
                    break

        elif piece_name == 'King':
            pass

        return moves


    def get_legal_moves(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.get_color() == color:
                    moves += self.get_possible_squares(piece)
        return moves
