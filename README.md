# chessai-learning
Python - Using self play to make a chess engine.

Log of functions and API's:

--------------------------------------------------Engine Class----------------------------------------------------\n
__init__(self)
Takes in nothing
Returns nothing

Creates self.board - 
self.board is 8 x 8 2D array. Each element is "None" or a chess piece object

Creates self.stack -
self.stack is a stack containing all pushed (nonfinalized) moves

Creates self.moves_made -
self.move_made is an int tracking total moves made in the game. Game terminates at 501 moves via the is_terminal function


__init_board__(self, board = None)
Takes in an optional board configuration
Returns nothing

If it has the optional board configuration it initalizes the chess board full of piece objects according to that configuraition. Without that argument it initializes a traditional chess board full of traditional chess pieces.

Game piece objects are initialized via the Piece class


__print_board__(self)
Takes in nothing
Returns nothing
No effect on rest of engine

print_board simply prints out the current state of the board. Empty squares are represented as '-'. 
Pieces are represented by the   following notation: (pawn: p, rook: r, knight:n, bishop: b, queen: q, king: k). 
Black pieces are represented by UPPERCASE letters. White pieces are represent by lowercase letters.


__in_check__(self,color)
Takes in the color of the king to be evaluated for check
Returns (True if in check, False if not in check)

Evaluates the position of the king of chosen color, determines if they are in check based on the current board position.


__get_board__(self)
Takes in nothing
Returns self.board

Returns the 2D array representing the current board state


__push_move__(self, move)
Takes in a move tuple
Returns nothing
Alters the boardstate

push_move takes in a move to make and any pieces that would be captured by that move. It pushes the move onto self.stack inorder to be removed later. It updates the board with chosen move

__pop_move__(self)
Takes in nothing
Returns nothing
Alters the game board

pop_move uses the self.stack stack to under the moves made by push_move. The pop_move undos these moves from the board and remove them from the move stack.


__update_board__(self, move)
Takes in a move tuple
Returns nothing
Alters the board state
