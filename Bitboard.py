import numpy as np

class Bitboard():
    def __init__(self):
        self.__init_board__()
        self.__init_mask__()


    def __init_board__(self):
        #Check king and queen, had confusion is this where we look in reverse?
        self.white_pawn = 0b0000000000000000000000000000000000000000000000001111111100000000 #65280
        self.white_rook = 0b0000000000000000000000000000000000000000000000000000000010000001 #129
        self.white_knight = 0b0000000000000000000000000000000000000000000000000000000001000010 #66
        self.white_bishop = 0b0000000000000000000000000000000000000000000000000000000000100100
        self.white_queen = 0b0000000000000000000000000000000000000000000000000000000000010000
        self.white_king = 0b0000000000000000000000000000000000000000000000000000000000001000

        self.black_pawn = 0b0000000011111111000000000000000000000000000000000000000000000000 #71776119061217280
        self.black_rook = 0b1000000100000000000000000000000000000000000000000000000000000000 #9295429630892703744
        self.black_knight = 0b0100001000000000000000000000000000000000000000000000000000000000 #4755801206503243776
        self.black_bishop = 0b0010010000000000000000000000000000000000000000000000000000000000
        self.black_queen = 0b0001000000000000000000000000000000000000000000000000000000000000
        self.black_king = 0b000100000000000000000000000000000000000000000000000000000000000


    def __init_mask__(self):
        #Confused about kings indian
        # self.L1_mask = 0b (01111111)x8 (11111110)x8
        # self.L2_mask = 0b (00111111)x8 (11111100)x8

        # self.R1_mask = 0b (01111111)x8 (11111110)x8
        # self.R2_mask = 0b (00111111)x8 (11111100)x8

        self.T1_mask = 0b0000000011111111111111111111111111111111111111111111111111111111
        self.T2_mask = 0b0000000000000000111111111111111111111111111111111111111111111111

        self.B1_mask = 0b1111111111111111111111111111111111111111111111111111111100000000
        self.B2_mask = 0b1111111111111111111111111111111111111111111111110000000000000000
    

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


    #Possibly unnesicarry once numbers are in correct format
    def print_bin(self,num):
        print(format(num,'64b'))


driver = Bitboard()
print(format(driver.get_all(),'64b'))