import numpy as np

class Bitboard():
    def __init__(self):
        self.__init_board__()
        self.__init_mask__()


    def __init_board__(self):
        self.white_pawns = np.uint64(0b0000000000000000000000000000000000000000000000001111111100000000) #65280
        self.white_rooks = np.uint64(0b0000000000000000000000000000000000000000000000000000000010000001) #129
        self.white_knights = np.uint64(0b0000000000000000000000000000000000000000000000000000000001000010) #66
        self.white_bishops = np.uint64(0b0000000000000000000000000000000000000000000000000000000000100100)
        self.white_queens = np.uint64(0b0000000000000000000000000000000000000000000000000000000000001000)
        self.white_kings = np.uint64(0b0000000000000000000000000000000000000000000000000000000000010000)

        self.black_pawns = np.uint64(0b0000000011111111000000000000000000000000000000000000000000000000) #71776119061217280
        self.black_rooks = np.uint64(0b1000000100000000000000000000000000000000000000000000000000000000) #9295429630892703744
        self.black_knights = np.uint64(0b0100001000000000000000000000000000000000000000000000000000000000) #4755801206503243776
        self.black_bishops = np.uint64(0b0010010000000000000000000000000000000000000000000000000000000000)
        self.black_queens = np.uint64(0b0000100000000000000000000000000000000000000000000000000000000000)
        self.black_kings = np.uint64(0b0001000000000000000000000000000000000000000000000000000000000000)


    def __init_mask__(self):
        self.col_mask = np.zeros((8,),dtype='uint64')
        self.fill_col_mask_arr()
        
        self.row_mask = np.zeros((8,),dtype='uint64')
        self.fill_row_mask_arr()

        self.diag_left_mask = np.zeros((15,),dtype='uint64')
        # self.fill_diag_left_mask_arr()

    def make_col_mask(self,mask):
        for i in range(8):
            mask = mask | mask << np.uint64(8)
        return(mask)

    def fill_col_mask_arr(self):
        for i in range(8):
            self.col_mask[7-i] = self.make_col_mask(np.uint64(1) << np.uint64(i))

    def make_row_mask(self,mask):
        for i in range(7):
            mask = mask | mask << np.uint64(1)
        return(mask)

    def fill_row_mask_arr(self):
        for i in range(8):
            self.row_mask[i] = self.make_row_mask(np.uint64(1) << np.uint64(8*i))

    def make_diag_left_mask(self,mask):
        self.print_chess_rep(mask)
        print('\n')

        BR_mask = ~((self.row_mask[0]) | (self.col_mask[7]))
        self.print_chess_rep(BR_mask)
        print('\n')

        self.print_chess_rep(mask & BR_mask)
        print('\n')
        for i in range(8):
            mask = mask | ((mask & BR_mask) >> np.uint64(7))
        return(mask)

    def get_all_white(self):
        all_white = self.white_pawns | self.white_rooks | self.white_knights | self.white_bishops | self.white_kings | self.white_queens
        return(all_white)


    def get_all_black(self):
        all_black = self.black_pawns | self.black_rooks | self.black_knights | self.black_bishops | self.black_kings | self.black_queens
        return(all_black)


    def get_all(self):
        white = self.get_all_white()
        black = self.get_all_black()
        all_pieces = white | black
        return(all_pieces)


    def print_chess_rep(self, num):
        for i in range(7, -1, -1):
            shifter = np.uint64(8 * i)
            row = (num & self.row_mask[i]) >> shifter
            print('{0:08b}'.format(row))

    # East:      >> 1
    # Southeast: << 7
    # South:     << 8
    # Southwest: << 9
    # West:      << 1
    # Northwest: >> 7
    # North:     >> 8
    # Northeast: >> 9

    # Takes in king_rep (bitboad representing that colors king locaiton)
    # Takes in same_occupied (bitboard representing all pieces of that color)
    # Returns bitboard representing all possible pre_check moves that the king can make
    def pre_check_king(self, king_rep, same_occupied):
        king_clip_file_0 = king_rep & self.col_mask[0]; 
        king_clip_file_7 = king_rep & self.col_mask[7]; 

        spot_0 = king_clip_file_7 << np.uint64(7) 
        spot_1 = king_loc << np.uint64(8) # down one
        spot_2 = king_clip_file_7 << np.uint64(9) # down left
        spot_3 = king_clip_file_7 << np.uint64(1) # left one

        spot_4 = king_clip_file_0 >> np.uint64(7)
        spot_5 = king_loc >> np.uint64(8)
        spot_6 = king_clip_file_0 >> np.uint64(9) 
        spot_7 = king_clip_file_0 >> np.uint64(1) # right one

        king_moves = spot_0 | spot_1 | spot_2 | spot_3 | spot_4 | spot_5 | spot_6 | spot_7 

        return king_moves & ~same_occupied;



driver = Bitboard()
# driver.print_chess_rep(driver.white_pawn | driver.black_pawn)
driver.print_chess_rep(driver.make_diag_left_mask(np.uint64(0b0000000000000000000000000000000000000000000000010000000000000000)))
# driver.print_chess_rep(driver.row_mask[0])
# print('\n')
# driver.print_chess_rep(driver.col_mask[7])