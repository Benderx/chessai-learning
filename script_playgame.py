import Engine
import Player
import time
import Piece


'''

engine.white_king = Piece.King(1)
engine.white_king_pos = (4, 7)

p1 = Piece.Pawn(1)
p2 = Piece.Pawn(1)
p3 = Piece.Pawn(-1)

white_queen = Piece.Queen(1)
board[7][4] = engine.white_king
board[6][4] = p1
board[6][5] = p2
#board[7][3] = white_queen

engine.black_king = Piece.King(-1)
engine.black_king_pos = (4, 0)
black_queen = Piece.Queen(-1)
board[4][1] = p3
board[0][4] = engine.black_king
board[4][0] = black_queen
'''
game_list = []

for x in range(1):
    board = [[None for x in range(8)] for y in range(8)]

    play_by_play = False

    winner = None
    engine = Engine.Engine()

    engine.white_king = Piece.King(1)
    engine.white_king_pos = (4, 7)

    p1 = Piece.Pawn(1)
    p2 = Piece.Pawn(1)
    p3 = Piece.Pawn(-1)

    white_queen = Piece.Queen(1)
    board[7][4] = engine.white_king
    #board[6][4] = p1
    #board[6][5] = p2
    #board[7][3] = white_queen

    engine.black_king = Piece.King(-1)
    engine.black_king_pos = (4, 0)
    black_queen = Piece.Queen(-1)
    black_rook1 = Piece.Rook(-1)
    board[1][4] = p3
    board[0][4] = engine.black_king
    #board[4][0] = black_queen
    #board[0][7] = black_rook1

    engine.init_board()

    PLAYER_ONE = Player.AiMinimax(1,engine)
    PLAYER_TWO = Player.AiRand(-1,engine)

    #print(PLAYER_TWO.evaluate(-1, 2))

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
                game_list.append((1,engine.get_game_length()))
            elif winner == -1:
                print("Results are in: Black wins")
                game_list.append((-1,engine.get_game_length()))
            else:
                print("Results are in: Draw")
                game_list.append((0,engine.get_game_length()))
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

f = open("tests.txt", 'w')
f.write(str(game_list))
