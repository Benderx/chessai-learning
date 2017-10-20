# chessai-learning
Python - Using self play to make a chess engine.

Log of functions and API's:

--------------------------------------------------Engine Class----------------------------------------------------

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

print_board(self)
  Takes in nothing
  Returns nothing
  No effect on rest of engine

  print_board simply prints out the current state of the board. Empty squares are represented as '-'. 
  Pieces are represented by the   following notation: (pawn: p, rook: r, knight:n, bishop: b, queen: q, king: k). 
  Black pieces are represented by UPPERCASE letters. White pieces are represent by lowercase letters.
