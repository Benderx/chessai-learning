import Engine
import Piece

import h5py as h5
import numpy as np

engine = Engine.Engine()

engine.init_board()
board = engine.get_board()

class BoardConverter():
	def __init__(self,engine,color=1):
		self.engine = engine
		self.con = np.zeros(72, dtype=np.int8)
		#0-63 are pieces
		#64-69 are who moved
			#White king, white rook 1, white rook 2
			#Black king, black rook 1, black rook 2
			#1 if moved and 0 if have not moved
		#70 is color to move
		#71 is last move
		self.con[71] = color
		self.encode_board()
		self.write_to_file()
		self.write_to_file(0,1)
		self.write_to_file(0,2)
		self.read_all()
		self.output = self.read_from_file()
		# print(self.con)
		# print(self.output)


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
		# print(self.con)

	#Consider moving name slot to self.
	def write_to_file(self,game=0, move=0):
		name = "Game"+str(game)
		moveNum = "Move"+str(move)
		file = h5.File(name,'a')
		file.create_dataset(moveNum, data = self.con)
		file.close()

	def read_from_file(self, game=0, move=0):
		name = "Game"+str(game)
		moveNum = "Move"+str(move)
		read_file = h5.File(name,'r')
		self.decoded_board = read_file[moveNum][:]
		read_file.close()

	def read_all(self, game=0):
		name = "Game"+str(game)
		read_file = h5.File(name,'r')
		for line in read_file:
			print(read_file[line][:])


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


driver = BoardConverter(engine)