class Piece():
	def __init__(self, color):
		self.color = color
		self.alive = True

	def get_color(self):
		return(self.color)

	def on_board(self):
		return(self.alive)

	def remove(self):
		self.alive = False

	def get_piece(self):
		raise Exception('This is not a piece') 


class Pawn(Piece):
	def __init__(self, color):
		super().__init__(color)

	def get_piece(self):
		return("Pawn")

class Rook(Piece):
	def __init__(self, color):
		super().__init__(color)
		self.moved = False

	def has_moved(self):
		return(self.moved)

	def get_piece(self):
		return("Rook")

class Knight(Piece):
	def __init__(self, color):
		super().__init__(color)

	def get_piece(self):
		return("Night")

class Bishop(Piece):
	def __init__(self, color):
		super().__init__(color)

	def get_piece(self):
		return("Bishop")

class King(Piece):
	def __init__(self, color):
		super().__init__(color)
		self.moved = False

	def get_piece(self):
		return("King")

	def has_moved(self):
		return(self.moved)

	def no_castle(self):
		self.moved = True

class Queen(Piece):
	def __init__(self, color):
		super().__init__(color)

	def get_piece(self):
		return("Queen")
