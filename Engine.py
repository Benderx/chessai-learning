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
        self.stack = []



    def init_board(self, board = None):
        if board:
            #Custom board state
            pass
        else:
            #Initialize basic chess board
            self.board[6][0] = Piece.Pawn(1)
            self.board[6][1] = Piece.Pawn(1)
            self.board[6][2] = Piece.Pawn(1)
            self.board[6][3] = Piece.Pawn(1)
            self.board[6][4] = Piece.Pawn(1)
            self.board[6][5] = Piece.Pawn(1)
            self.board[6][6] = Piece.Pawn(1)
            self.board[6][7] = Piece.Pawn(1)

            black_pawn_1 = Piece.Pawn(-1)
            black_pawn_2 = Piece.Pawn(-1)
            black_pawn_3 = Piece.Pawn(-1)
            black_pawn_4 = Piece.Pawn(-1)
            black_pawn_5 = Piece.Pawn(-1)
            black_pawn_6 = Piece.Pawn(-1)
            black_pawn_7 = Piece.Pawn(-1)
            black_pawn_8 = Piece.Pawn(-1)
            self.board[1][0] = black_pawn_1
            self.board[1][1] = black_pawn_2
            self.board[1][2] = black_pawn_3
            self.board[1][3] = black_pawn_4
            self.board[1][4] = black_pawn_5
            self.board[1][5] = black_pawn_6
            self.board[1][6] = black_pawn_7
            self.board[1][7] = black_pawn_8

            white_rook_1 = Piece.Rook(1)
            white_rook_2 = Piece.Rook(1)
            self.board[7][0] = white_rook_1
            self.board[7][7] = white_rook_2

            black_rook_1 = Piece.Rook(-1)
            black_rook_2 = Piece.Rook(-1)
            self.board[0][0] = black_rook_1
            self.board[0][7] = black_rook_2

            white_knight_1 = Piece.Knight(1)
            white_knight_2 = Piece.Knight(1)
            self.board[7][1] = white_knight_1
            self.board[7][6] = white_knight_2

            black_knight_1 = Piece.Knight(-1)
            black_knight_2 = Piece.Knight(-1)
            self.board[0][1] = black_knight_1
            self.board[0][6] = black_knight_2

            white_bishop_1 = Piece.Bishop(1)
            white_bishop_2 = Piece.Bishop(1)
            self.board[7][2] = white_bishop_1
            self.board[7][5] = white_bishop_2

            black_bishop_1 = Piece.Bishop(-1)
            black_bishop_2 = Piece.Bishop(-1)
            self.board[0][2] = black_bishop_1
            self.board[0][5] = black_bishop_2

            white_king = Piece.King(1)
            self.white_king_pos = (7, 3)
            white_queen = Piece.Queen(1)
            self.board[7][3] = white_king
            self.board[7][4] = white_queen

            black_king = Piece.King(-1)
            self.black_king_pos = (0, 3)
            black_queen = Piece.Queen(-1)
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
            pos = self.black_king_pos
        else:
            pos = self.white_king_pos

        #Check to left of king
        for i in range(pos[0]-1,-1,-1):
            pass



    def get_board(self):
        return self.board


    def push_move(self, move):
        self.stack.append((move, self.board[move[1][1]][move[1][0]]))
        self.update_board(move)


    def pop_move(self):
        info = self.stack.pop()
        move = info[0]
        piece = info[1]
        self.undo_board(move, piece)


    def update_board(self, move):
        if len(move) == 1: # castling
            pass
        elif len(move) == 3: # pawn promotion
            pass
        else: # normal move
            if self.board[move[0][1]][move[0][0]].get_piece() == 'King': # if moving king
                if self.board[move[0][1]][move[0][0]].get_color() == 1:
                    self.white_king_pos = move[1]
                else:
                    self.black_king_pos = move[1]
            self.board[move[1][1]][move[1][0]] = self.board[move[0][1]][move[0][0]]
            self.board[move[0][1]][move[0][0]] = None


    def undo_board(self, move, piece):
        if len(move) == 1: # castling
            pass
        elif len(move) == 3: # pawn promotion
            pass
        else: # normal move
            if self.board[move[1][1]][move[1][0]].get_piece() == 'King': # if moving king
                if self.board[move[1][1]][move[1][0]].get_color() == 1:
                    self.white_king_pos = move[0]
                else:
                    self.black_king_pos = move[0]
            self.board[move[0][1]][move[0][0]] = self.board[move[1][1]][move[1][0]]
            self.board[move[1][1]][move[1][0]] = piece


    def invert_color(self, color):
        return(-color)


    def promotions(self, color, pos, to_pos):
        promos = []
        promos.append((pos, to_pos, Knight(color, pos)))
        promos.append((pos, to_pos, Rook(color, pos)))
        promos.append((pos, to_pos, Queen(color, pos)))
        promos.append((pos, to_pos, Bishop(color, pos)))
        return promos


    def get_possible_squares(self, piece, pos):
        moves = []
        init_x = pos[0]
        init_y = pos[1]
        piece_name = piece.get_piece()


        if piece_name == 'Pawn':
            if piece.get_color() == 1:
                x_1 = init_x
                y_1 = init_y - 1
                if y_1 > -1:
                    space = self.board[y_1][x_1]
                    if not space:
                        if y_1 == 0:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_1, y_1))
                        else:
                            moves.append(((init_x, init_y), (x_1, y_1)))

                x_2 = init_x + 1
                y_2 = init_y - 1
                if x_2 < 8 and y_2 > -1:
                    space = self.board[y_2][x_2]
                    if space and space.get_color() != piece.get_color():
                        if y_2 == 0:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_2, y_2))
                        else:
                            moves.append(((init_x, init_y), (x_2, y_2)))

                x_3 = init_x - 1
                y_3 = init_y - 1
                if x_3 > -1 and y_3 > -1:
                    space = self.board[y_3][x_3]
                    if space and space.get_color() != piece.get_color():
                        if y_3 == 0:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_3, y_3))
                        else:
                            moves.append(((init_x, init_y), (x_3, y_3)))

                x_4 = init_x
                y_4 = init_y - 2
                space = self.board[y_4][x_4]
                inter_space = self.board[y_4+1][x_4]
                if not space and not inter_space:
                    moves.append(((init_x, init_y), (x_4, y_4)))
            else:
                x_1 = init_x
                y_1 = init_y + 1
                if y_1 < 8:
                    space = self.board[y_1][x_1]
                    if not space:
                        if y_1 == 7:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_1, y_1))
                        else:
                            moves.append(((init_x, init_y), (x_1, y_1)))

                x_2 = init_x + 1
                y_2 = init_y + 1
                if x_2 < 8 and y_2 < 8:
                    space = self.board[y_2][x_2]
                    if space and space.get_color() != piece.get_color():
                        if y_2 == 7:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_2, y_2))
                        else:
                            moves.append(((init_x, init_y), (x_2, y_2)))

                x_3 = init_x - 1
                y_3 = init_y + 1
                if x_3 > -1 and y_3 < 8:
                    space = self.board[y_3][x_3]
                    if space and space.get_color() != piece.get_color():
                        if y_3 == 7:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_3, y_3))
                        else:
                            moves.append(((init_x, init_y), (x_3, y_3)))

                x_4 = init_x
                y_4 = init_y + 2
                space = self.board[y_4][x_4]
                inter_space = self.board[y_4-1][x_4]
                if not space and not inter_space:
                    moves.append(((init_x, init_y), (x_4, y_4)))

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
            if not piece.has_moved:
                square_right_1 = self.board[init_y][init_x + 1]
                square_right_2 = self.board[init_y][init_x + 2]
                square_right_3 = self.board[init_y][init_x + 3]

                if not square_right_1 and not square_right_2 and square_right_3:
                    if square_right_3.get_piece() == 'Rook' and not square_right_3.has_moved():
                        moves.append('castle')

                square_left_1 = self.board[init_y][init_x - 1]
                square_left_2 = self.board[init_y][init_x - 2]
                square_left_3 = self.board[init_y][init_x - 3]
                square_left_4 = self.board[init_y][init_x - 4]

                if not square_left_1 and not square_left_2 and not square_left_3 and square_left_4:
                    if square_left_4.get_piece() == 'Rook' and not square_left_4.has_moved():
                        moves.append('qastle')


            x_1 = init_x + 1
            y_1 = init_y - 1
            if x_1 < 8 and y_1 > -1:
                space = self.board[y_1][x_1]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_1, y_1)))

            x_2 = init_x + 1
            y_2 = init_y
            if x_2 < 8:
                space = self.board[y_2][x_2]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_2, y_2)))

            x_3 = init_x + 1
            y_3 = init_y + 1
            if x_3 < 8 and y_3 < 8:
                space = self.board[y_3][x_3]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_3, y_3)))

            x_4 = init_x
            y_4 = init_y + 1
            if y_4 < 8:
                space = self.board[y_4][x_4]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_4, y_4)))

            x_5 = init_x - 1
            y_5 = init_y + 1
            if x_5 > -1 and y_5 < 8:
                space = self.board[y_5][x_5]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_5, y_5)))

            x_6 = init_x - 1
            y_6 = init_y
            if x_6 > -1:
                space = self.board[y_6][x_6]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_6, y_6)))

            x_7 = init_x - 1
            y_7 = init_y - 1
            if x_7 > -1 and y_7 > -1:
                space = self.board[y_7][x_7]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_7, y_7)))

            x_8 = init_x
            y_8 = init_y - 1
            if y_8 > -1:
                space = self.board[y_8][x_8]
                if not space or space.get_color() != piece.get_color():
                    moves.append(((init_x, init_y), (x_8, y_8)))

        return moves


    # KNOWN ISSUES:
    #       En passant has no implementation
    #       Castling does not check if it castles through check

    def get_legal_moves(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.get_color() == color:
                    # RETURNS A LIST OF POSSIBLE MOVES
                    # PAWN PROMOTION WILL RETURN AS (pawn_pos, promotion_pos, Piece)
                    # CASTLING WILL RETURN AS ("castle") or ("qastle")
                    # EVERYTHING ELSE RETURNS AS (piece_pos, to_piece_pos)
                    moves += self.get_possible_squares(piece, (col, row))

        # checking if move puts you in check
        final_moves = []
        for move in moves:
            if move[0] == type(""): # castling edge case
                pass
            else:
                self.push_move(move)
                if not self.in_check(color):
                    final_moves.append(move)
                self.pop_move()
        return final_moves
