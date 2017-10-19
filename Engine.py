class Engine():
    def __init__(self):
        self.board = [['0' for x in range(8)] for y in range(8)]


    def print_final(self):
        for i in self.board:
            print(i)


    def is_terminal(self, color, moves):
        


    def get_board(self):
        return self.board


    def push_move(self,move,color):
        self.stack.append(move)
        self.update_board(move,color)


    def pop_move(self):
        move = self.stack.pop()
        self.undo_move(move)


    def update_board(self, move, color):
        


    def undo_move(self, move):
        


    def valid_move(self, move):
        


    def invert_color(self,color):
        if color == 'w':
            return('b')
        else:
            return('w')

    def get_legal_moves(self):
        