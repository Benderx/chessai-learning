import Piece

# -1 will represent black
# 1 will represent white
# init_board will take in optional argument board, and initilize self.board
#            to default position (or to the optional argument if provided)
# Position is in (x,y) board is in [y][x]

debug_check = False
debug_king = False
debug_square1 = False

class Engine():
    def __init__(self):
        #Board is accessed using [y][x] notation
        self.board = [[None for x in range(8)] for y in range(8)]
        self.stack = []
        self.moves_made = 0
        self.enpassant = {}


    def init_board(self, board = None):
        if board:
            self.board = board
            #Custom board state
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
            self.white_pawn_arr = []
            for i in self.board[6]:
                self.white_pawn_arr.append(i)

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
            self.black_pawn_arr = []
            for i in self.board[1]:
                self.black_pawn_arr.append(i)

            self.white_rook_1 = Piece.Rook(1,0)
            self.white_rook_2 = Piece.Rook(1,1)
            self.board[7][0] = self.white_rook_1
            self.board[7][7] = self.white_rook_2

            self.black_rook_1 = Piece.Rook(-1,0)
            self.black_rook_2 = Piece.Rook(-1,1)
            self.board[0][0] = self.black_rook_1
            self.board[0][7] = self.black_rook_2

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

            self.white_king = Piece.King(1)
            self.white_king_pos = (4, 7)
            white_queen = Piece.Queen(1)
            self.board[7][4] = self.white_king
            self.board[7][3] = white_queen

            self.black_king = Piece.King(-1)
            self.black_king_pos = (4, 0)
            black_queen = Piece.Queen(-1)
            self.board[0][4] = self.black_king
            self.board[0][3] = black_queen


    def print_board(self):
        for row in self.board:
            a = []
            for col in row:
                if col == None:
                    a.append('-')
                else:
                    if col.get_color() == 1:
                        a.append(col.get_piece()[0].lower())
                    else:
                        a.append(col.get_piece()[0].upper())
            print(''.join(a))


    def in_check(self, color):
        #Takes in color of player's turn
        #Ensures they do not end turn in check
        #True for check
        if color == -1:
            pos = self.black_king_pos
            pos_enemy = self.white_king_pos
        else:
            pos = self.white_king_pos
            pos_enemy = self.black_king_pos

        if debug_check: print("I am color:", color, "I am at:", pos)

        pos_x = pos[0]
        pos_y = pos[1]

        ############### Check rooks and non-diagnal queens ###############
        #Check to left of king
        for x in range(pos_x-1,-1,-1):
            if self.board[pos_y][x]:
                local_piece = self.board[pos_y][x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Rook" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Rook":
                            print("Enemy rook at:",(x,pos_y),"got me.")
                        else:
                            print("Enemy queen at:",(x,pos_y),"got me.")
                    return(True)
                break

        #Check to right of king
        for x in range(pos_x+1, 8):
            if self.board[pos_y][x]:
                local_piece = self.board[pos_y][x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Rook" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Rook":
                            print("Enemy rook at:",(x,pos_y),"got me.")
                        else:
                            print("Enemy queen at:",(x,pos_y),"got me.")
                    return(True)
                break

        #Check above king
        for y in range(pos_y-1,-1,-1):
            if self.board[y][pos_x]:
                local_piece = self.board[y][pos_x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Rook" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Rook":
                            print("Enemy rook at:",(pos_x,y),"got me.")
                        else:
                            print("Enemy queen at:",(pos_x,y),"got me.")
                    return(True)
                break

        #Check below king
        for y in range(pos_y+1,8):
            if self.board[y][pos_x]:
                local_piece = self.board[y][pos_x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Rook" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Rook":
                            print("Enemy rook at:",(pos_x,y),"got me.")
                        else:
                            print("Enemy queen at:",(pos_x,y),"got me.")
                    return(True)
                break


        #Check knights
        up1,down1,left1,right1 = (False, False, False, False)
        up2,down2,left2,right2 = (False, False, False, False)
        if pos_x + 1 <= 7: 
            right1 = True
            if pos_x + 2 <= 7: 
                right2 = True

        if pos_x - 1 >= 0:
            left1 = True
            if pos_x - 2 >= 0: 
                left2 = True

        if pos_y - 1 >= 0:
            up1 = True
            if pos_y - 2 >= 0: 
                up2 = True

        if pos_y + 1 <= 7:
            down1 = True
            if pos_y + 2 <= 7:
                down2 = True

        if up2 and right1:
            if self.board[pos_y-2][pos_x+1]:
                local_piece = self.board[pos_y-2][pos_x+1]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x+1,pos_y-2),"got me.")
                    return(True)

        if up1 and right2:
            if self.board[pos_y-1][pos_x+2]:
                local_piece = self.board[pos_y-1][pos_x+2]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x+2,pos_y-1),"got me.")
                    return(True)

        if down1 and right2:
            if self.board[pos_y+1][pos_x+2]:
                local_piece = self.board[pos_y+1][pos_x+2]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x+2,pos_y+1),"got me.")
                    return(True)

        if down2 and right1:
            if self.board[pos_y+2][pos_x+1]:
                local_piece = self.board[pos_y+2][pos_x+1]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x+1,pos_y+2),"got me.")
                    return(True)

        if down2 and left1:
            if self.board[pos_y+2][pos_x-1]:
                local_piece = self.board[pos_y+2][pos_x-1]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x-1,pos_y+2),"got me.")
                    return(True)

        if down1 and left2:
            if self.board[pos_y+1][pos_x-2]:
                local_piece = self.board[pos_y+1][pos_x-2]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x-2,pos_y+1),"got me.")
                    return(True)

        if up1 and left2:
            if self.board[pos_y-1][pos_x-2]:
                local_piece = self.board[pos_y-1][pos_x-2]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x-1,pos_y-2),"got me.")
                    return(True)

        if up2 and left1:
            if self.board[pos_y-2][pos_x-1]:
                local_piece = self.board[pos_y-2][pos_x-1]
                if local_piece.get_piece() == "Night" and local_piece.get_color() != color:
                    if debug_check:
                        print("Enemy night at:",(pos_x-1,pos_y-2),"got me.")
                    return(True)


        #Check Bishops and queens (and pawns)
        #Check up/left
        x = pos_x-1
        y = pos_y-1
        while x >= 0 and y >= 0:
            if self.board[y][x]:
                local_piece=self.board[y][x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Bishop" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Bishop":
                            print("Enemy bishop at:",(x,y),"got me.")
                        else:
                            print("Enemy queen at:",(x,y),"got me.")
                    return(True)
                break
            x -= 1
            y -= 1

        #Check up/right
        x = pos_x+1
        y = pos_y-1
        while x < 8 and y >= 0:
            if self.board[y][x]:
                local_piece=self.board[y][x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Bishop" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Bishop":
                            print("Enemy bishop at:",(x,y),"got me.")
                        else:
                            print("Enemy queen at:",(x,y),"got me.")
                    return(True)
                break
            x += 1
            y -= 1

        #Check down/right
        x = pos_x+1
        y = pos_y+1
        while x < 8 and y < 8:
            if self.board[y][x]:
                local_piece=self.board[y][x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Bishop" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Bishop":
                            print("Enemy bishop at:",(x,y),"got me.")
                        else:
                            print("Enemy queen at:",(x,y),"got me.")
                    return(True)
                break
            x += 1
            y += 1

        #Check down/left
        x = pos_x-1
        y = pos_y+1
        while x >= 0 and y < 8:
            if self.board[y][x]:
                local_piece=self.board[y][x]
                if local_piece.get_color() != color and (local_piece.get_piece() == "Bishop" or local_piece.get_piece() == "Queen"):
                    if debug_check:
                        if local_piece.get_piece() == "Bishop":
                            print("Enemy bishop at:",(x,y),"got me.")
                        else:
                            print("Enemy queen at:",(x,y),"got me.")
                    return(True)
                break
            x -= 1
            y += 1


        #Check pawn
        if color == -1 and pos_y < 7:
            if pos_x - 1 >= 0 and self.board[pos_y+1][pos_x-1] and self.board[pos_y+1][pos_x-1].get_piece() == "Pawn" and self.board[pos_y+1][pos_x-1].get_color() == 1:
                if debug_check:
                    print("Enemy pawn at:",(pos_x-1,pos_y+1),"got me.")
                return(True)
            if pos_x + 1 < 8 and self.board[pos_y+1][pos_x+1] and self.board[pos_y+1][pos_x+1].get_piece() == "Pawn" and self.board[pos_y+1][pos_x+1].get_color() == 1:
                if debug_check:
                    print("Enemy pawn at:",(pos_x+1,pos_y+1),"got me.")
                return(True)

        elif color == 1 and pos_y > 0: 
            if pos_x - 1 >= 0 and self.board[pos_y-1][pos_x-1] and self.board[pos_y-1][pos_x-1].get_piece() == "Pawn" and self.board[pos_y-1][pos_x-1].get_color() == -1:
                if debug_check:
                    print("Enemy pawn at:",(pos_x-1,pos_y-1),"got me.")
                return(True)

            if pos_x + 1 < 8 and self.board[pos_y-1][pos_x+1] and self.board[pos_y-1][pos_x+1].get_piece() == "Pawn" and self.board[pos_y-1][pos_x+1].get_color() == -1:
                if debug_check:
                    print("Enemy pawn at:",(pos_x+1,pos_y-1),"got me.")
                return(True)
        #Check other king Last possible
        if abs(pos_x-pos_enemy[0]) < 2 and abs(pos_y-pos_enemy[1]) < 2:
            if debug_check: print("Enemy King at:",pos, "got me.")
            return(True)
        return(False)


    def get_board(self):
        return self.board


    def push_move(self, move):
        identity = move[3]
        if identity == 'normal'or identity == 'promotion': # Normal moves and enpassant
            self.stack.append((move, self.board[move[1][1]][move[1][0]]))
        else:
            self.stack.append((move, 'yaboi')) # Castling moves
        self.perform_move(move)


    def pop_move(self):
        info = self.stack.pop()
        move = info[0]
        identity = move[3]
        if identity == 'normal' or identity == 'promotion': # Normal moves and enpassant
            piece = info[1]
        else: # castling
            piece = None
        self.undo_move(move, piece)


    def perform_move(self, move):
        self.moves_made += 1
        pos1 = move[0]
        pos2 = move[1]
        piece = move[2]
        identity = move[3]

        if identity[2:] == 'astle': # castling
            if identity[0] == 'w':
                y = 7
                self.white_king.add_move()
            else:
                y = 0
                self.black_king.add_move()
            x1_king = 4

            if identity[1:] == 'castle':
                x2_king = 6
                x1_rook = 7
                x2_rook = 5
                if identity[0] == 'w':
                    self.white_king_pos = (6, 7)
                else:
                    self.black_king_pos = (6, 0)
            else:
                x2_king = 2
                x1_rook = 0
                x2_rook = 3
                if identity[0] == 'w':
                    self.white_king_pos = (2, 7)
                else:
                    self.black_king_pos = (2, 0)

            self.board[y][x2_king] = self.board[y][x1_king]
            self.board[y][x2_rook] = self.board[y][x1_rook]
            self.board[y][x1_king] = None
            self.board[y][x1_rook] = None
            return

        x1 = pos1[0]
        y1 = pos1[1]
        x2 = pos2[0]
        y2 = pos2[1]

        square1 = self.board[y1][x1]
        square2 = self.board[y2][x2]

        if identity == 'promotion': # pawn promotion
            self.board[y1][x1] = None
            self.board[y2][x2] = piece
            return

        # normal move
        if identity == 'enpassant': # enpassant
            self.board[y1][x2] = None

        if debug_square1: print("x and y value of square is:", (x1, y1))

        if square1.get_piece() == 'King': # if moving king
            square1.add_move()
            if square1.get_color() == 1:
                self.white_king_pos = pos2
            else:
                self.black_king_pos = pos2

        if square1.get_piece() == 'Rook': # if moving rook
            square1.add_move()

        if len(self.enpassant) > 0:
            self.enpassant = {}
        if square1.get_piece() == 'Pawn':
            if abs(y2 - y1) == 2:
                self.enpassant[x2] = True
        
        self.board[y2][x2] = square1
        self.board[y1][x1] = None


    def undo_move(self, move, old_piece):
        self.moves_made -= 1
        pos1 = move[0]
        pos2 = move[1]
        piece = move[2]
        identity = move[3]

        if identity[2:] == 'astle': # castling
            if identity[0] == 'w':
                y = 7
                self.white_king.sub_move()
            else:
                y = 0
                self.black_king.sub_move()
            x2_king = 4

            if identity[1:] == 'castle':
                x1_king = 6
                x2_rook = 7
                x1_rook = 5
                if identity[0] == 'w':
                    self.white_king_pos = (4, 7)
                else:
                    self.black_king_pos = (4, 0)
            else:
                x1_king = 2
                x2_rook = 0
                x1_rook = 3
                if identity[0] == 'w':
                    self.white_king_pos = (4, 7)
                else:
                    self.black_king_pos = (4, 0)

            self.board[y][x2_king] = self.board[y][x1_king]
            self.board[y][x2_rook] = self.board[y][x1_rook]
            self.board[y][x1_king] = None
            self.board[y][x1_rook] = None
            return

        x1 = move[0][0]
        y1 = move[0][1]
        x2 = move[1][0]
        y2 = move[1][1]

        square1 = self.board[y1][x1]
        square2 = self.board[y2][x2]

        if identity == 'promotion': # pawn promotion
            color = self.board[y2][x2].get_color()
            self.board[y1][x1] = Piece.Pawn(color)
            self.board[y2][x2] = old_piece
            return

        # normal move
        if identity == 'enpassant': # enpassant
            self.board[y1][x2] = Piece.Pawn(self.invert_color(square2.get_color()))
            self.enpassant[x2] = True

        if square2.get_piece() == 'King': # if moving king
            if square2.get_color() == 1:
                self.white_king_pos = pos1
            else:
                self.black_king_pos = pos1
            square2.sub_move()

        if square2.get_piece() == 'Rook':
            square2.sub_move()

        if square2.get_piece() == 'Pawn':
            if abs(y2 - y1) == 2:
                # self.enpassant[x2] = False
                self.enpassant.pop(x2, None)

        self.board[y1][x1] = square2
        self.board[y2][x2] = old_piece


    def invert_color(self, color):
        return(-color)


    def promotions(self, color, pos, to_pos):
        promos = []
        promos.append(self.create_move(pos, to_pos, Piece.Knight(color)))
        promos.append(self.create_move(pos, to_pos, Piece.Rook(color)))
        promos.append(self.create_move(pos, to_pos, Piece.Queen(color)))
        promos.append(self.create_move(pos, to_pos, Piece.Bishop(color)))
        return promos


    def create_move(self, pos1, pos2, extra):
        if extra == None:  # the move is a normal move (pos1, pos2, None)
            return tuple([pos1, pos2, None, 'normal'])

        if isinstance(extra, Piece.Piece):  # the move is a promotion move (pos1, pos2, Piece)
            return tuple([pos1, pos2, extra, 'promotion'])

        if isinstance(extra, str): # the move is an enpassant promotion move (pos1, pos2, Piece)
            if extra == 'enpassant':
                return tuple([pos1, pos2, None, extra])
            else:
                return tuple([None, None, None, extra])

        raise Exception('Not well formed move in create_move()')


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
                            moves.append(self.create_move((init_x, init_y), (x_1, y_1), None))

                x_2 = init_x + 1
                y_2 = init_y - 1
                if x_2 < 8 and y_2 > -1:
                    space = self.board[y_2][x_2]
                    if not space:
                        if y_2 == 2 and x_2 in self.enpassant:
                            moves.append(self.create_move((init_x, init_y), (x_2, y_2), 'enpassant'))
                    elif space.get_color() != piece.get_color():
                        if y_2 == 0:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_2, y_2))
                        else:
                            moves.append(self.create_move((init_x, init_y), (x_2, y_2), None))

                x_3 = init_x - 1
                y_3 = init_y - 1
                if x_3 > -1 and y_3 > -1:
                    space = self.board[y_3][x_3]
                    if not space:
                        if y_3 == 2 and x_3 in self.enpassant:
                            moves.append(self.create_move((init_x, init_y), (x_3, y_3), 'enpassant'))
                    elif space and space.get_color() != piece.get_color():
                        if y_3 == 0:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_3, y_3))
                        else:
                            moves.append(self.create_move((init_x, init_y), (x_3, y_3), None))

                if init_y == 6:
                    x_4 = init_x
                    y_4 = init_y - 2
                    space = self.board[y_4][x_4]
                    inter_space = self.board[y_4+1][x_4]
                    if not space and not inter_space:
                        moves.append(self.create_move((init_x, init_y), (x_4, y_4), None))

            else:
                x_1 = init_x
                y_1 = init_y + 1
                if y_1 < 8:
                    space = self.board[y_1][x_1]
                    if not space:
                        if y_1 == 7:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_1, y_1))
                        else:
                            moves.append(self.create_move((init_x, init_y), (x_1, y_1), None))

                x_2 = init_x + 1
                y_2 = init_y + 1
                if x_2 < 8 and y_2 < 8:
                    space = self.board[y_2][x_2]
                    if not space:
                        if y_2 == 5 and x_2 in self.enpassant:
                            moves.append(self.create_move((init_x, init_y), (x_2, y_2), 'enpassant'))
                    elif space.get_color() != piece.get_color():
                        if y_2 == 7:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_2, y_2))
                        else:
                            moves.append(self.create_move((init_x, init_y), (x_2, y_2), None))

                x_3 = init_x - 1
                y_3 = init_y + 1
                if x_3 > -1 and y_3 < 8:
                    space = self.board[y_3][x_3]
                    if not space:
                        if y_3 == 5 and x_3 in self.enpassant:
                            moves.append(self.create_move((init_x, init_y), (x_3, y_3), 'enpassant'))
                    elif space.get_color() != piece.get_color():
                        if y_3 == 7:
                            moves += self.promotions(piece.get_color(), (init_x, init_y), (x_3, y_3))
                        else:
                            moves.append(self.create_move((init_x, init_y), (x_3, y_3), None))

                if init_y == 1:
                    x_4 = init_x
                    y_4 = init_y + 2
                    space = self.board[y_4][x_4]
                    inter_space = self.board[y_4-1][x_4]
                    if not space and not inter_space:
                        moves.append(self.create_move((init_x, init_y), (x_4, y_4), None))

        elif piece_name == 'Rook':
            for y in range(1, 8):
                if init_y + y > 7:
                    break
                space = self.board[init_y + y][init_x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y + y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y + y), None))
                    break

            for y in range(1, 8):
                if init_y - y < 0:
                    break
                space = self.board[init_y - y][init_x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y - y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y - y), None))
                    break

            for x in range(1, 8):
                if init_x + x > 7:
                    break
                space = self.board[init_y][init_x + x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x + x, init_y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x + x, init_y), None))
                    break

            for x in range(1, 8):
                if init_x - x < 0:
                    break
                space = self.board[init_y][init_x - x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x - x, init_y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x - x, init_y), None))
                    break

        elif piece_name == 'Night':
            x_1 = init_x + 1
            y_1 = init_y - 2
            if x_1 < 8 and y_1 > -1:
                space = self.board[y_1][x_1]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_1, y_1), None))

            x_2 = init_x + 2
            y_2 = init_y - 1
            if x_2 < 8 and y_2 > -1:
                space = self.board[y_2][x_2]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_2, y_2), None))

            x_3 = init_x + 2
            y_3 = init_y + 1
            if x_3 < 8 and y_3 < 8:
                space = self.board[y_3][x_3]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_3, y_3), None))

            x_4 = init_x + 1
            y_4 = init_y + 2
            if x_4 < 8 and y_4 < 8:
                space = self.board[y_4][x_4]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_4, y_4), None))

            x_5 = init_x - 1
            y_5 = init_y + 2
            if x_5 > -1 and y_5 < 8:
                space = self.board[y_5][x_5]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_5, y_5), None))

            x_6 = init_x - 2
            y_6 = init_y + 1
            if x_6 > -1 and y_6 < 8:
                space = self.board[y_6][x_6]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_6, y_6), None))

            x_7 = init_x - 2
            y_7 = init_y - 1
            if x_7 > -1 and y_7 > -1:
                space = self.board[y_7][x_7]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_7, y_7), None))

            x_8 = init_x - 1
            y_8 = init_y - 2
            if x_8 > -1 and y_8 > -1:
                space = self.board[y_8][x_8]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_8, y_8), None))

        elif piece_name == 'Bishop':
            for inc in range(1, 8):
                if init_x + inc > 7 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x + inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y + inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y + inc), None))
                    break

            for inc in range(1, 8):
                if init_x + inc > 7 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x + inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y - inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y - inc), None))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x - inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y + inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y + inc), None))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x - inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y - inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y - inc), None))
                    break

        elif piece_name == 'Queen':
            for y in range(1, 8):
                if init_y + y > 7:
                    break
                space = self.board[init_y + y][init_x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y + y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y + y), None))
                    break

            for y in range(1, 8):
                if init_y - y < 0:
                    break
                space = self.board[init_y - y][init_x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y - y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x, init_y - y), None))
                    break

            for x in range(1, 8):
                if init_x + x > 7:
                    break
                space = self.board[init_y][init_x + x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x + x, init_y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x + x, init_y), None))
                    break

            for x in range(1, 8):
                if init_x - x < 0:
                    break
                space = self.board[init_y][init_x - x]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x - x, init_y), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x - x, init_y), None))
                    break


            for inc in range(1, 8):
                if init_x + inc > 7 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x + inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y + inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y + inc), None))
                    break

            for inc in range(1, 8):
                if init_x + inc > 7 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x + inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y - inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x + inc, init_y - inc), None))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y + inc > 7:
                    break
                space = self.board[init_y + inc][init_x - inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y + inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y + inc), None))
                    break

            for inc in range(1, 8):
                if init_x - inc < 0 or init_y - inc < 0:
                    break
                space = self.board[init_y - inc][init_x - inc]

                if space is None:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y - inc), None))
                elif space.get_color() == piece.get_color():
                    break
                else:
                    moves.append(self.create_move((init_x, init_y), (init_x - inc, init_y - inc), None))
                    break

        elif piece_name == 'King':
            x_1 = init_x + 1
            y_1 = init_y - 1
            if x_1 < 8 and y_1 > -1:
                space = self.board[y_1][x_1]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_1, y_1), None))

            x_2 = init_x + 1
            y_2 = init_y
            if x_2 < 8:
                space = self.board[y_2][x_2]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_2, y_2), None))

            x_3 = init_x + 1
            y_3 = init_y + 1
            if x_3 < 8 and y_3 < 8:
                space = self.board[y_3][x_3]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_3, y_3), None))

            x_4 = init_x
            y_4 = init_y + 1
            if y_4 < 8:
                space = self.board[y_4][x_4]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_4, y_4), None))

            x_5 = init_x - 1
            y_5 = init_y + 1
            if x_5 > -1 and y_5 < 8:
                space = self.board[y_5][x_5]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_5, y_5), None))

            x_6 = init_x - 1
            y_6 = init_y
            if x_6 > -1:
                space = self.board[y_6][x_6]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_6, y_6), None))

            x_7 = init_x - 1
            y_7 = init_y - 1
            if x_7 > -1 and y_7 > -1:
                space = self.board[y_7][x_7]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_7, y_7), None))

            x_8 = init_x
            y_8 = init_y - 1
            if y_8 > -1:
                space = self.board[y_8][x_8]
                if not space or space.get_color() != piece.get_color():
                    moves.append(self.create_move((init_x, init_y), (x_8, y_8), None))

        return moves


    def get_legal_moves(self, color):
        # Add all moves but castles
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.get_color() == color:
                    # RETURNS A LIST OF POSSIBLE MOVES TUPLES DEFINED AS (pos1, pos2, identity)
                    # PAWN PROMOTION WILL RETURN AS (pos1, pos2, Piece())
                    # ENAPSSANT WILL RETURN AS (pos1, pos2, 'enpassant')
                    # EVERYTHING ELSE RETURNS AS (pos1, pos2, None)
                    moves += self.get_possible_squares(piece, (col, row))


        # Add castles 
        # CASTLING WILL RETURN AS ("castle") or ("qastle")
        castle_possibles = self.can_castle(color)
        if castle_possibles[0]:
            if color == 1:
                # check_filtered_moves.append(tuple(['wcastle']))
                moves.append(self.create_move(None, None, 'wcastle'))
            else:
                # check_filtered_moves.append(tuple(["bcastle"]))
                moves.append(self.create_move(None, None, 'bcastle'))
        if castle_possibles[1]:
            if color == 1:
                moves.append(self.create_move(None, None, 'wqastle'))
            else:
                moves.append(self.create_move(None, None, 'bqastle'))


        # checking if move puts you in check
        check_filtered_moves = []
        for move in moves:
            self.push_move(move)
            if not self.in_check(color):
                check_filtered_moves.append(move)
            self.pop_move()
        
        return check_filtered_moves


    def is_terminal(self, color, moves):
        #Takes in moves and turn takers color
        #Returns None if ongoing, zero if draw, or color of winner
        if self.get_game_length() > 250:
            return(0)
        elif len(moves) != 0:
            return(None)
        else:
            if self.in_check(color):
                return(self.invert_color(color))
            else:
                return(0)


    def get_game_length(self):
        return(self.moves_made)


    def can_castle(self, color):
        #Returns (True or False, True or False) for (can_castle,can_qastle)
        castle = True
        qastle = True

        if color == -1:
            king = self.black_king
            pos_y = 0
            r1 = self.board[pos_y][0]
            r2 = self.board[pos_y][7]
            # pos_y = self.black_king_pos[1]
        else:
            king = self.white_king
            pos_y = 7
            r1 = self.board[pos_y][0]
            r2 = self.board[pos_y][7]
            # pos_y = self.white_king_pos[1]

        if king.get_moved() > 0:
            return((False,False))
        if self.board[pos_y][5] or self.board[pos_y][6]:
            castle = False
        if self.board[pos_y][1] or self.board[pos_y][2] or self.board[pos_y][3]:
            qastle = False

        if castle and (not r1 or r1.get_piece() != 'Rook' or r1.get_moved() > 0):
            castle = False
        if qastle and (not r2 or r2.get_piece() != 'Rook' or r2.get_moved() > 0):
            qastle = False

        if castle:
            move = self.create_move((4, pos_y), (5, pos_y), None)
            self.push_move(move)
            if self.in_check(color):
                castle = False
            self.pop_move()

        if qastle: 
            move = self.create_move((4, pos_y), (3, pos_y), None)
            self.push_move(move)
            if self.in_check(color):
                qastle = False
            self.pop_move()

        result = (castle, qastle)
        return(result)