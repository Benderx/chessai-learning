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
    def __init__(self, color, num=3):
        super().__init__(color)
        self.moved = 0
        self.num = num

    def get_moved(self):
        return(self.moved)

    def get_piece(self):
        return("Rook")

    def add_move(self):
        self.moved += 1

    def sub_move(self):
        self.moved -= 1

    def get_rook_num(self):
        return(self.num)

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
        self.moved = 0

    def get_piece(self):
        return("King")

    def get_moved(self):
        return(self.moved)

    def add_move(self):
        self.moved += 1

    def sub_move(self):
        self.moved -= 1

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_piece(self):
        return("Queen")