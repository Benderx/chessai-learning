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

    def fill_diag_left_mask_arr(self):
        start = np.uint64(1) << np.uint64(7)
        
        for i in range(8):
            self.diag_left_mask[i] = make_diag_left_mask(start)
            start = start << np.uint64(8)
        start = start >> np.uint64(1)

        for j in range(8,16):
            self.diag_left_mask[j] = make_diag_left_mask(start)
            start = start >> np.uint64(1)

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


    def reverse_8_bit(self, row):
        num = np.uint8(row)
        reverse_num = np.uint8(row)
        one_8 = np.uint8(1)
        count = np.uint8(8 - 1);
         
        num = num >> one_8
        while(num):
            # print('iter_num', np.binary_repr(num))
            # print('iter_rev', np.binary_repr(reverse_num))
            # print('iter_count', count)
            # print()
            reverse_num = reverse_num << one_8    
            reverse_num = reverse_num | (num & one_8)
            num = num >> one_8
            count -= one_8

        # print('iter_num', np.binary_repr(num))
        # print('final_rev', np.binary_repr(reverse_num))
        # print('final_count', count)

        # print(count)
        reverse_num = reverse_num << count
        return reverse_num


    # def test_lol(self):
    #     rev = self.reverse_8_bit(0b00000110)
    #     print(np.binary_repr(rev))


    def print_chess_rep(self, num):
        for i in range(7, -1, -1):
            shifter = np.uint64(8 * i)
            row = (num & self.row_mask[i]) >> shifter
            rev = self.reverse_8_bit(row)
            print('{0:08b}'.format(rev))
            # print(rev.dtype)
            # print(np.binary_repr(rev))


    # East:      << 1
    # Southeast: >> 7
    # South:     >> 8
    # Southwest: >> 9
    # West:      >> 1
    # Northwest: << 7
    # North:     << 8
    # Northeast: << 9

    # Takes in king_rep (bitboad representing that colors king locaiton)
    # Takes in same_occupied (bitboard representing all pieces of that color)
    # Returns bitboard representing all possible pre_check moves that the king can make
    def pre_check_king(self, king_rep, same_occupied):
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


        return king_moves
        # return king_moves & ~same_occupied;


    def get_king_moves(self, color):
        if color == 1:
            return self.pre_check_king(self.white_kings, self.get_all_white())
        else:
            return self.pre_check_king(self.black_kings, self.get_all_black())



driver = Bitboard()
# driver.print_chess_rep(driver.white_pawn | driver.black_pawn)
# driver.print_chess_rep(driver.make_diag_left_mask(np.uint64(0b0000000000000000000000000000000000000000000000010000000000000000)))



# driver.print_chess_rep(driver.row_mask[0])

print('white king pos')
driver.print_chess_rep(driver.white_kings)
print('white king legal moves')
driver.print_chess_rep(driver.get_king_moves(1))
