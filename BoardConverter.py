import Engine
import Piece

import h5py as h5
import numpy as np

class BoardConverter():
    def __init__(self,engine,game,move,color=1,title = "Data"):
        self.engine = engine
        self.game = game
        self.con = np.zeros(72, dtype=np.int16)
        self.title = title
        #0-63 are pieces
        #64-69 are who moved
            #White king, white rook 1, white rook 2
            #Black king, black rook 1, black rook 2
            #1 if moved and 0 if have not moved
        #70 is color to move
        #71 is last move
        self.con[70] = color
        self.con[71] = move
        self.encode_board()
        self.write_to_file()


    def encode_board(self):
        i = 0
        board = self.engine.get_board()
        for y in range(len(board)):
            for x in range(len(board[0])):
                local_piece = board[y][x]
                if local_piece:
                    self.con[i] = self.piece_to_val(local_piece)
                else:
                    self.con[i] = 0
                i += 1

    #Consider using libver="latest" for preformence
    def write_to_file(self):
        group = "Game"+str(self.game)
        moveNum = "Move"+"%03d" % self.con[71]
        print("BoardConverter Move:",moveNum)
        file = h5.File(self.title,'a')
        file.require_group(group)
        file[group].require_dataset(moveNum, data = self.con,shape=(72,),dtype=np.int16)
        file.close()


    def piece_to_val(self,piece_obj):
        piece = piece_obj.get_piece()
        color = piece_obj.get_color()

        if piece == "Pawn":
            val = 1
        elif piece == "Rook":
            val = 2
            self.has_moved(piece_obj,'r')
        elif piece == "Night":
            val = 3
        elif piece == "Bishop":
            val = 4
        elif piece == "Queen":
            val = 5
        elif piece == "King":
            val = 6
            self.has_moved(piece_obj)
        return(val*color)


    def has_moved(self,piece_obj,p_type='k'):
        index = 64
        if piece_obj.get_color() == -1:
            index += 3
        if p_type == 'r':
            index += piece_obj.get_rook_num()
        if piece_obj.get_moved():
            self.con[index] = 1
        else:
            self.con[index] = 0

class BoardDecoder():
    def __init__(self,title="Data"):
        self.title = title


    def read_game(self,game):
        group = "Game"+str(game)
        read_file = h5.File(self.title,'r')
        for move in read_file[group]:
            yield(read_file[group][move][:])


    def read_all(self):
        read_file = h5.File(self.title,'r')
        for group in read_file:
            print(read_file[group])
            for move in read_file[group]:
                print(move)
                # print(read_file[group][move][:])