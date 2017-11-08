import Bitboard as bb
import numpy as np

#Boards taken from https://lichess.org/editor

def convert_lichess_2int(board_string):
    temp = np.zeros((12,), dtype='uint64')
    
    nums = set("12345678")
    white = set("RNBQKP")
    black = set("rnbqkp")

    power = 0
    rows = board_string.split('/')

    for row in rows[::-1]:
        for char in row:
            if char in nums:
                power += int(char)
            elif char in white:
                if char == 'P':
                    num = 0
                elif char == 'R':
                    num = 1
                elif char == 'N':
                    num = 2
                elif char == 'B':
                    num = 3
                elif char == 'Q':
                    num = 4
                elif char == 'K':
                    num = 5
                temp[num] += np.uint64(2**power)
                power += 1

            else:
                if char == 'p':
                    num = 6
                elif char == 'r':
                    num = 7
                elif char == 'n':
                    num = 8
                elif char == 'b':
                    num = 9
                elif char == 'q':
                    num = 10
                elif char == 'k':
                    num = 11

                temp[num] += np.uint64(2**power)
                power += 1
    print(temp)
    return(temp)

load = "rnbqkbnr/p1pppppp/8/1p6/4P3/5P2/PPPP2PP/RNBQKBNR w KQkq -"
board = load[:-9]
print("Given load: ",load)
print("Lichess Board Info: ",board)
np_board_arr = convert_lichess_2int(board)
print("Creating board...")
engine = bb.BitboardEngine(np_board_arr)
print("\nEngine board generated:")
engine.print_chess_rep(engine.get_all())
print("\nPrint White Pieces")
engine.print_chess_rep(engine.get_all_white())
print("\nPrint White Pawns")
engine.print_chess_rep(engine.white_pawns)
print("\nPrint White Rooks")
engine.print_chess_rep(engine.white_rooks)
print("\nPrint Black Pawns")
engine.print_chess_rep(engine.black_pawns)
print("\nPrint Black Rooks")
engine.print_chess_rep(engine.black_rooks)