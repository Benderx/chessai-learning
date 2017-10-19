class Piece():
	def __init__(self, color, position):
		self.color = color
		self.pos = position
		self.alive = True

	def get_color(self):
		return(self.color)

	def get_position(self):
		return(self.pos)

	def update_position(self, new_pos):
		self.pos = new_pos

	def on_board(self):
		return(self.alive)

	def remove(self):
		self.alive = False

	def get_piece(self):
		raise Exception('This is not a piece') 


class Pawn(Piece):
	def __init__(self, color, position):
		super().__init__(color, position)

	def get_piece(self):
		return("Pawn")

class Rook(Piece):
	def __init__(self, color, position):
		super().__init__(color, position)

	def get_piece(self):
		return("Rook")

class Knight(Piece):
	def __init__(self, color, position):
		super().__init__(color, position)

	def get_piece(self):
		return("Night")

class Bishop(Piece):
	def __init__(self, color, position):
		super().__init__(color, position)

	def get_piece(self):
		return("Bishop")

class King(Piece):
	def __init__(self, color, position):
		super().__init__(color, position)
		self.moved = False

	def get_piece(self):
		return("King")

	def has_moved(self):
		return(self.moved)

	def no_castle(self):
		self.moved = True

class Queen(Piece):
	def __init__(self, color, position):
		super().__init__(color, position)

	def get_piece(self):
		return("Queen")
