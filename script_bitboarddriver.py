import Bitboard as bb
import numpy as np


def form_board(wp, wr, wn, wb, wq, wk, bp, br, bn, bb, bq, bk):
      temp = np.zeros((12,), dtype='uint64')
      temp[0] = wp
      temp[1] = wr
      temp[2] = wn
      temp[3] = wb
      temp[4] = wq
      temp[5] = wk
      temp[6] = bp
      temp[7] = br
      temp[8] = bn
      temp[9] = bb
      temp[10] = bq
      temp[11] = bk
      return temp

def gen_scenario_1_board():
      white_pawns = np.uint64(0b0000000000000000000000000000000000000000000000001111111100000000) #65280
      white_rooks = np.uint64(0b0000000000000000000000000000000000000100000000000000000010000001) #129
      white_nights = np.uint64(0b0000000000000000000000000000000000000000000000000000000001000010) #66
      white_bishops = np.uint64(0b0000000000000000000000000000000000100000000000000000000000100100)
      white_queens = np.uint64(0b0000000000000000000000000000000000000000000000000000000000001000)
      white_kings = np.uint64(0b0000000000000000000000000000000000000000000000000000000000010000)

      black_pawns = np.uint64(0b0000000011111111000000000000000000000000000000000000000000000000) #71776119061217280
      black_rooks = np.uint64(0b1000000100000000000000000000000000000000000000000000000000000000) #9295429630892703744
      black_nights = np.uint64(0b0100001000000000000000000000000000000000000000000000000000000000) #4755801206503243776
      black_bishops = np.uint64(0b0010010000000000000000000000000000000000000000000000000000000000)
      black_queens = np.uint64(0b0000100000000000000000000000000000000000000000000000000000000000)
      black_kings = np.uint64(0b0001000000000000000000000000000000000000000000000000000000000000)

      board = form_board(white_pawns, white_rooks, white_nights, white_bishops, white_queens, white_kings,
            black_pawns, black_rooks, black_nights, black_bishops, black_queens, black_kings)
      return board

board = gen_scenario_1_board()
engine = bb.BitboardEngine(board)
engine.print_chess_rep(engine.get_all())
# engine.print_chess_rep(engine.get_all())
# engine.print_chess_rep(engine.white_pawn | engine.black_pawn)

print('white king pos')
engine.print_chess_rep(engine.white_kings)
print('white king legal moves')
engine.print_chess_rep(engine.get_king_moves(-1))