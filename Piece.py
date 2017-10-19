class Piece():
	def __init__(self, color, engine, position, value):
		self.engine = engine
		self.color = color
		self.pos = position
		self.val = value
		self.alive = True

	def get_color(self):
		return(self.color)

	def get_position(self):
		return(self.pos)

	def update_position(self, new_pos):
		self.pos = new_pos

	def get_val(self):
		return(self.value)

	def on_board(self):
		return(self.alive)

	def remove(self):
		self.alive = False


class Pawn(Piece):
	def __init__(self, color, engine, position, value):
		super().__init__(color, engine, position, value)

class Rook(Piece):
	def __init__(self, color, engine, position, value):
		super().__init__(color, engine, position, value)

class Knight(Piece):
	def __init__(self, color, engine, position, value):
		super().__init__(color, engine, position, value)

class Bishop(Piece):
	def __init__(self, color, engine, position, value):
		super().__init__(color, engine, position, value)

class King(Piece):
	def __init__(self, color, engine, position, value):
		super().__init__(color, engine, position, value)
		self.moved = False

	def has_moved(self):
		return(self.moved)

	def no_castle(self):
		self.moved = True

class Queen(Piece):
	def __init__(self, color, engine, position, value):
		super().__init__(color, engine, position, value)