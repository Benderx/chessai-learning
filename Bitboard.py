import numpy as np
from enum import Enum

class Piece(Enum):
    NONE = 0
    PAWN = 1
    ROOK = 2
    NIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6

class MoveType(Enum):
    REGULAR = 0
    CASTLE = 1
    ENPASSANT = 2
    PROMOTION = 3


class BitboardEngine():
    def __init__(self):
        self.init_board()
        self.init_engine()


    def __init__(self, board_data):
        self.fill_board(board_data)
        self.init_engine()


    def init_engine(self):
        self.max_move_length = 500 # This assumes there are only 500 possible legal moves at any one time (affects move array intilization)
        self.in_check = np.uint8(0)
        self.init_mask()


    def init_board(self):
        self.white_pawns = np.uint64(0b0000000000000000000000000000000000000000000000001111111100000000) #65280
        self.white_rooks = np.uint64(0b0000000000000000000000000000000000000000000000000000000010000001) #129
        self.white_nights = np.uint64(0b0000000000000000000000000000000000000000000000000000000001000010) #66
        self.white_bishops = np.uint64(0b0000000000000000000000000000000000000000000000000000000000100100)
        self.white_queens = np.uint64(0b0000000000000000000000000000000000000000000000000000000000001000)
        self.white_kings = np.uint64(0b0000000000000000000000000000000000000000000000000000000000010000)

        self.black_pawns = np.uint64(0b0000000011111111000000000000000000000000000000000000000000000000) #71776119061217280
        self.black_rooks = np.uint64(0b1000000100000000000000000000000000000000000000000000000000000000) #9295429630892703744
        self.black_nights = np.uint64(0b0100001000000000000000000000000000000000000000000000000000000000) #4755801206503243776
        self.black_bishops = np.uint64(0b0010010000000000000000000000000000000000000000000000000000000000)
        self.black_queens = np.uint64(0b0000100000000000000000000000000000000000000000000000000000000000)
        self.black_kings = np.uint64(0b0001000000000000000000000000000000000000000000000000000000000000)


    def fill_board(self, board_data):
        self.white_pawns = board_data[0]
        self.white_rooks = board_data[1]
        self.white_nights = board_data[2]
        self.white_bishops = board_data[3] 
        self.white_queens = board_data[4] 
        self.white_kings = board_data[5] 

        self.black_pawns = board_data[6]
        self.black_rooks = board_data[7]  
        self.black_nights = board_data[8]  
        self.black_bishops = board_data[9] 
        self.black_queens = board_data[10] 
        self.black_kings = board_data[11] 



    def init_mask(self):
        self.col_mask = np.zeros((8,), dtype='uint64')
        self.fill_col_mask_arr()
        
        self.row_mask = np.zeros((8,), dtype='uint64')
        self.fill_row_mask_arr()

        self.diag_left_mask = np.zeros((15,), dtype='uint64')
        self.fill_diag_left_mask_arr()
        #Diag left masks start on left side and moves from left to right, top to bottom
        #[0] corresponds to bottom left corner
        #[0]-[7] moves up y axis along x=0
        #[7] is top left corner
        #[7]-[14] moves across x-axis along y=7
        #[14] is top right corner

        self.diag_right_mask = np.zeros((15,), dtype='uint64')
        self.fill_diag_right_mask_arr()
        #Diag right masks start on bottom side and moves from left to right, bottom to top
        #[0] corresponds to bottom right corner
        #[0]-[7] moves down the x axis along y=0
        #[7] is bottom left corner
        #[7]-[14] moves up the y-axis along x=0
        #[14] is top left corner


    def make_col_mask(self, mask):
        for i in range(8):
            mask = mask | mask << np.uint64(8)
        return(mask)


    def fill_col_mask_arr(self):
        for i in range(8):
            self.col_mask[i] = self.make_col_mask(np.uint64(1) << np.uint64(i))


    def make_row_mask(self, mask):
        for i in range(7):
            mask = mask | mask << np.uint64(1)
        return(mask)


    def fill_row_mask_arr(self):
        for i in range(8):
            self.row_mask[i] = self.make_row_mask(np.uint64(1) << np.uint64(8*i))


    def make_diag_left_mask(self,mask):
        BR_mask = ~((self.row_mask[0]) | (self.col_mask[7]))

        for i in range(8):
            mask = mask | ((mask & BR_mask) >> np.uint64(7))
        return(mask)


    def fill_diag_left_mask_arr(self):
        start = np.uint64(1)
        
        for i in range(8):
            self.diag_left_mask[i] = self.make_diag_left_mask(start)
            if i!= 7: start = start << np.uint64(8)
        start = start << np.uint64(1)

        for j in range(8,15):
            self.diag_left_mask[j] = self.make_diag_left_mask(start)
            start = start << np.uint64(1)


    def make_diag_right_mask(self,mask):
        TR_mask = ~((self.row_mask[7]) | (self.col_mask[7]))

        for i in range(8):
            mask = mask | ((mask & TR_mask) << np.uint64(9))
        return(mask)


    def fill_diag_right_mask_arr(self):
        start = np.uint64(1) << np.uint64(7)
        for i in range(8):
            self.diag_right_mask[i] = self.make_diag_right_mask(start)
            if i!= 7: start = start >> np.uint64(1)
        start = start << np.uint64(8)

        for j in range(8,15):          
            self.diag_right_mask[j] = self.make_diag_right_mask(start)
            start = start << np.uint64(8)


    def get_all_white(self):
        all_white = self.white_pawns | self.white_rooks | self.white_nights | self.white_bishops | self.white_kings | self.white_queens
        return(all_white)


    def get_all_black(self):
        all_black = self.black_pawns | self.black_rooks | self.black_nights | self.black_bishops | self.black_kings | self.black_queens
        return(all_black)


    def get_all(self):
        white = self.get_all_white()
        black = self.get_all_black()
        all_pieces = white | black
        return(all_pieces)


    # Takes in move information
    #     start : int 0-63 : Square moved piece started on
    #     end : int 0-63 : Square moved piece ended on
    #     m_type: int 0-3 : Type of move made
    #     piece: int 0-4 : Piece taken in move
    #     promotion: int 2-5 : Piece to promote pawn to
    # Return a np.uint32 representing all above info
    # Alters nothing

    def encode_move(self, start, end, m_type, piece, promotion):
        encode_start = np.uint8(start)
        encode_end = np.uint16(end) << np.uint8(6)
        encode_type = np.uint32(m_type) << np.uint8(12)
        encode_piece = np.uint32(piece) << np.uint8(14)
        encode_promotion = np.uint32(promotion) << np.uint(17)
        return(encode_start & encode_end & encode_type & encode_piece & encode_promotion)
    # Takes in a np.uint32 move
    # Returns square number moved piece originated from
    # Alters nothing
    def decode_from(self,move):
        return(move & np.uint8(63))


    # Takes in a np.uint32 move
    # Returns square number moved piece travels to
    # Alters nothing
    def decode_to(self,move):
        return((move >> np.uint8(6)) & np.uint8(63))


    # Takes in a np.uint32 move
    # Returns type of move made
    # Alters nothing
    def decode_type(self,move):
        return((move >> np.uint8(12)) & np.uint8(3)) 


    # Takes in a np.uint32 move
    # Returns any piece taken by move
    # Alters nothing
    def decode_piece(self,move):
        return((move >> np.uint8(14)) & np.uint8(7)) 

    # Takes in a np.uint32 move
    # Returns new piece pawn promoted to
    # Alters nothing
    def decode_promo(self,move):
        return((move >> np.uint8(17)) & np.uint8(3))


    # Takes in a bitboard and will return the bitboard representing only the least significant bit.
    # Example: the initial white_nights bitboard, the least significant 1 occurs at index 1 (...00001000010)
    # therefore simply return ((lots of zeros)00000000000010)
    # YOU MAY ASSUME A 1 EXISTS, (0000000000000000000) will not be given
    def lsb_digit(self):
        return((num & -num).bit_length()-1)

    # Takes in a bitboard
    # Returns a bitboard with soley the least significant bit = 1
    # All other bits = 0
    # Alters nothing
    def lsb_board(self):
        return(num & -num)

    # See above, except return the move_list significant bit bitboard
    def msb(self):
        pass


    # Reverses a uint8 number, like this (00110000 -> 00001100)
    # To improve, possibly just not(11111111 - num)??? 
    def reverse_8_bit(self, row):
        num = np.uint8(row)
        reverse_num = np.uint8(row)
        one_8 = np.uint8(1)
        count = np.uint8(7);
         
        num = num >> one_8
        while(num):
            reverse_num = reverse_num << one_8    
            reverse_num = reverse_num | (num & one_8)
            num = num >> one_8
            count -= one_8
        reverse_num = reverse_num << count
        return reverse_num
        # return ~(np.uint8(255) - np.uint8(row))


    def print_chess_rep(self, num):
        for i in range(7, -1, -1):
            shifter = np.uint64(8 * i)
            row = (num & self.row_mask[i]) >> shifter
            rev = self.reverse_8_bit(row)
            print('{0:08b}'.format(rev))


    # East:      << 1
    # Southeast: >> 7
    # South:     >> 8
    # Southwest: >> 9
    # West:      >> 1
    # Northwest: << 7
    # North:     << 8
    # Northeast: << 9


    # Takes in a move, alters the BitboardEngine's representation to the NEXT state based on the CURRENT move action
    def push_move(self, move):
        pass


    # Takes in a move, alters the BitboardEngine's representation to the PREVIOUS state based on the LAST move action
    def push_move(self, move):
        pass


    def get_square(self, piece, color):
        if color: # white
            if piece == Piece.KING:
                return self.white_kings
            else:
                pass
        else: # black
            if piece == Piece.KING:
                return self.black_kings
            else:
                pass


    # Some hueristics have been met, the only way to check if a move is legal or not, we must make it.
    def check_legal(self, move):
        pass


    # Returns a bitboard of pieces that are pinned against their king 
    def pinned_pieces(self, color):
        pass


    # Generates and fills move_list for a color before checking checks
    def generate_pre_check_moves(self, color, move_list):
        king_loc = self.pre_check_king_bitboard()
        return all_pre_check_moves


    # Generates and returns a list of legal moves for a color
    def generate_legal_moves(self, color):
        all_legal_moves = np.zeros((self.max_move_length,), dtype='uint32')
        last_move_index = 0

        pinned = self.pinned_pieces(color);
        king_square = self.get_square(Piece.KING, color)

        if self.in_check:
            pass
            # generate<EVASIONS>(pos, moveList)         last_move_index returned
        else:
            pass
            # generate<NON_EVASIONS>(pos, moveList)     last_move_index returned

        move_iter = 0
        while move_iter < last_move_index:
            move = all_legal_moves[move_iter]
            if (pinned or self.decode_from(move) == king_square or self.decode_type(move) == MoveType.ENPASSANT) and not self.check_legal(move):
                last_move_index -= 1
                all_legal_moves[move_iter] = all_legal_moves[last_move_index]

        return all_legal_moves


    def pop_moves(self, moves, move_board, curr_pos, t, piece, promo):
        while(board):
            move = self.lsb_board(board)
            self.encode_move(self.lsb_digit(curr_pos), self.lsb_digit(move_board), t, piece, promo)
            board = board & (~move)


    def rook_attacks(self):
        # o^(o-2s)
        pass


    def bishop_attacks(self):
        pass


    # Takes in king_rep (bitboad representing that colors king location)
    # Takes in same_occupied (bitboard representing all pieces of that color)
    # Returns bitboard representing all possible pre_check moves that the king can make
    def pre_check_king_bitboard(self, king_rep, same_occupied):
        king_mask_file_0 = king_rep & ~self.col_mask[0]
        king_mask_file_7 = king_rep & ~self.col_mask[7] 

        spot_0 = king_mask_file_7 >> np.uint64(7) # Southeast
        spot_1 = king_rep >> np.uint64(8) # South
        spot_2 = king_mask_file_7 >> np.uint64(9) # Southwest
        spot_3 = king_mask_file_7 >> np.uint64(1) # West

        spot_4 = king_mask_file_0 << np.uint64(7) # Northwest
        spot_5 = king_rep << np.uint64(8) # North
        spot_6 = king_mask_file_0 << np.uint64(9) # Northeast
        spot_7 = king_rep << np.uint64(1) # East

        king_moves = spot_0 | spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 | spot_7 

        return king_moves & ~same_occupied;


    def get_king_moves(self, color):
        if color == 1:
            return self.pre_check_king_bitboard(self.white_kings, self.get_all_white())
        else:
            return self.pre_check_king_bitboard(self.black_kings, self.get_all_black())



    # Takes in night_rep (bitboad representing that colors night location)
    # Takes in same_occupied (bitboard representing all pieces of that color)
    # Returns bitboard representing all possible pre_check moves that that night can make
    def pre_check_night(self, king_rep, same_occupied):
        pass
        # spot_1_clip = tbls->ClearFile[FILE_A] & tbls->ClearFile[FILE_B];
        # spot_2_clip = tbls->ClearFile[FILE_A];
        # spot_3_clip = tbls->ClearFile[FILE_H];
        # spot_4_clip = tbls->ClearFile[FILE_H] & tbls->ClearFile[FILE_G];

        # spot_5_clip = tbls->ClearFile[FILE_H] & tbls->ClearFile[FILE_G];
        # spot_6_clip = tbls->ClearFile[FILE_H];
        # spot_7_clip = tbls->ClearFile[FILE_A];
        # spot_8_clip = tbls->ClearFile[FILE_A] & tbls->ClearFile[FILE_B];

        # spot_1 = (night_loc & spot_1_clip) << 6;
        # spot_2 = (night_loc & spot_2_clip) << 15;
        # spot_3 = (night_loc & spot_3_clip) << 17;
        # spot_4 = (night_loc & spot_4_clip) << 10;

        # spot_5 = (night_loc & spot_5_clip) >> 6;
        # spot_6 = (night_loc & spot_6_clip) >> 15;
        # spot_7 = (night_loc & spot_7_clip) >> 17;
        # spot_8 = (night_loc & spot_8_clip) >> 10;

        # nightValid = spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 |
        #                 spot_7 | spot_8;

        # /* compute only the places where the night can move and attack. The
        #     caller will determine if this is a white or black night. */
        # return nightValid & ~own_side;
