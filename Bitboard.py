import numpy as np

class Bitboard():
    def __init__(self):
        self.__init_board__()
        self.__init_mask__()


    def __init_board__(self):
        self.white_pawn = np.uint64(0b0000000000000000000000000000000000000000000000001111111100000000) #65280
        self.white_rook = np.uint64(0b0000000000000000000000000000000000000000000000000000000010000001) #129
        self.white_knight = np.uint64(0b0000000000000000000000000000000000000000000000000000000001000010) #66
        self.white_bishop = np.uint64(0b0000000000000000000000000000000000000000000000000000000000100100)
        self.white_queen = np.uint64(0b0000000000000000000000000000000000000000000000000000000000001000)
        self.white_king = np.uint64(0b0000000000000000000000000000000000000000000000000000000000010000)

        self.black_pawn = np.uint64(0b0000000011111111000000000000000000000000000000000000000000000000) #71776119061217280
        self.black_rook = np.uint64(0b1000000100000000000000000000000000000000000000000000000000000000) #9295429630892703744
        self.black_knight = np.uint64(0b0100001000000000000000000000000000000000000000000000000000000000) #4755801206503243776
        self.black_bishop = np.uint64(0b0010010000000000000000000000000000000000000000000000000000000000)
        self.black_queen = np.uint64(0b0000100000000000000000000000000000000000000000000000000000000000)
        self.black_king = np.uint64(0b0001000000000000000000000000000000000000000000000000000000000000)


    def __init_mask__(self):
        self.col_mask = np.zeros((8,),dtype='uint64')
        self.fill_col_mask_arr()
        
        self.row_mask = np.zeros((8,),dtype='uint64')
        self.fill_row_mask_arr()

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

    def get_all_white(self):
        all_white = self.white_pawn | self.white_rook | self.white_knight | self.white_bishop | self.white_king | self.white_queen
        return(all_white)


    def get_all_black(self):
        all_black = self.black_pawn | self.black_rook | self.black_knight | self.black_bishop | self.black_king | self.black_queen
        return(all_black)


    def get_all(self):
        white = self.get_all_white()
        black = self.get_all_black()
        all_pieces = white | black
        return(all_pieces)


    # def print_row(self, num, row):
    #     slide_forward = 0 << i * 8
    #     slide_back = 56 >> i * 8
    #     print('{0:08b}'.format((num << slide_forward) >> slide_back))


    def print_chess_rep(self, num):
        for i in range(7, -1, -1):
            shifter = np.uint64(8 * i)
            row = (num & self.row_mask[i]) >> shifter
            print('{0:08b}'.format(row))

    def psuedo_king(self, king_rep):
        pass



driver = Bitboard()
driver.print_chess_rep(driver.white_pawn | driver.black_pawn)