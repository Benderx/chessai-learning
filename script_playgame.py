import Engine
import Player
import time
import Piece

board = [[None for x in range(8)] for y in range(8)]




play_by_play = False

winner = None
engine = Engine.Engine()


engine.white_king = Piece.King(1)
engine.white_king_pos = (4, 7)
white_queen = Piece.Queen(1)
board[7][4] = engine.white_king
board[7][3] = white_queen

engine.black_king = Piece.King(-1)
engine.black_king_pos = (4, 0)
black_queen = Piece.Queen(-1)
board[0][4] = engine.black_king
board[0][3] = black_queen

engine.init_board(board)

PLAYER_ONE = Player.AiRand(1,engine)
PLAYER_TWO = Player.AiMinimax(-1,engine)

players = [PLAYER_ONE,PLAYER_TWO]

turn = 0

print("Inital Boardstate:")
engine.print_board()

while True:
    if play_by_play:
        input("")

    possible_moves = engine.get_legal_moves(players[turn].get_color())
    winner = engine.is_terminal(players[turn].get_color(), possible_moves)
    print("\n\nBoardstate:")
    engine.print_board()
    print("Current players turn:", players[turn].get_color())
    # print("All moves:\n",possible_moves)
    if winner != None:
        if winner == 1:
            print("Results are in: White wins")
        elif winner == -1:
            print("Results are in: Black wins")
        else:
            print("Results are in: Draw")
        break
    move = players[turn].get_move(possible_moves)
    print("Move:", move)
    if move[0] != None:
        print('Piece moved:', engine.get_board()[move[0][1]][move[0][0]].get_piece())
    else:
        print('Piece moved:', 'castle or something')
    engine.perform_move(move)
    print("Boardstate:")
    engine.print_board()
    print('\n')

    turn = 1-turn
    print(engine.get_game_length())
    if play_by_play:
        input("")
    # time.sleep(1)
